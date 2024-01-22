from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
# —------—
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, ValidationError, fields

app = Flask(__name__)
ma = Marshmallow(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Vacancy(db.Model):
    __tablename__ = 'vacancies'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class VacancySchema(Schema):
    id = fields.Integer()
    text = fields.String()
    date_added = fields.DateTime()
    user_id = fields.Integer()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    vacancies = db.relationship('Vacancy', backref='user', lazy='dynamic')
    # obj = db.Column(db.String)


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    date_created = fields.DateTime()
    vacancies = fields.List(fields.Nested(VacancySchema))
    # obj = fields.List(fields.Dict())


user_schema = UserSchema()
users_schema = UserSchema(many=True)
vacancy_schema = VacancySchema()
vacancies_schema = VacancySchema(many=True)


@app.route('/users')
def users():
    users = User.query.all()

    return users_schema.dump(users)


@app.route('/users/<user_id>')
def user(user_id):
    user = User.query.filter(User.id == user_id).first()

    return user_schema.dump(user)


@app.route('/create-user', methods=['POST'])
def create_user():
    request_data = request.get_json()

    try:
        validated_data = user_schema.load(request_data)
    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    new_user = User(email=validated_data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201


@app.route('/vacancies')
def vacancies():
    all_vacancies = Vacancy.query.all()

    return vacancies_schema.dump(all_vacancies)


@app.route('/user-vacancies/<user_id>')
def user_vacancies(user_id):
    user_vacancies = Vacancy.query.filter(Vacancy.user_id == user_id).all()

    return vacancies_schema.dump(user_vacancies)


@app.route('/create-vacancy', methods=['POST'])
def create_vacancy():
    request_data = request.get_json()

    try:
        validated_data = vacancy_schema.load(request_data)
    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    new_vacancy = Vacancy(
        text=validated_data['text'], user_id=validated_data['user_id'])
    db.session.add(new_vacancy)
    db.session.commit()

    return jsonify({'message': 'Vacancy added successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
