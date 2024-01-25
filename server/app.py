import json
from datetime import datetime

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
# —------—
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, ValidationError, fields

# from schemas import JobVacancySchema

app = Flask(__name__)
ma = Marshmallow(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# class Vacancy(db.Model):
#     __tablename__ = 'vacancies'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     description = db.Column(db.String)
#     salary = db.Column(db.JSON, nullable=True)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Vacancy(db.Model):
    __tablename__ = 'vacancies'

    id = db.Column(db.Integer, primary_key=True)
    hh_id = db.Column(db.Integer)
    premium = db.Column(db.Boolean)
    billing_type = db.Column(db.JSON)
    relations = db.Column(db.JSON)
    name = db.Column(db.String)
    insider_interview = db.Column(db.String, nullable=True)
    response_letter_required = db.Column(db.Boolean)
    area = db.Column(db.JSON)
    salary = db.Column(db.JSON)
    type = db.Column(db.JSON)
    address = db.Column(db.JSON)
    allow_messages = db.Column(db.Boolean)
    experience = db.Column(db.JSON)
    schedule = db.Column(db.JSON)
    employment = db.Column(db.JSON)
    department = db.Column(db.String, nullable=True)
    contacts = db.Column(db.String, nullable=True)
    description = db.Column(db.String)
    branded_description = db.Column(db.String, nullable=True)
    vacancy_constructor_template = db.Column(db.String, nullable=True)
    key_skills = db.Column(db.JSON)
    accept_handicapped = db.Column(db.Boolean)
    accept_kids = db.Column(db.Boolean)
    archived = db.Column(db.Boolean)
    response_url = db.Column(db.String, nullable=True)
    specializations = db.Column(db.JSON)
    professional_roles = db.Column(db.JSON)
    code = db.Column(db.String, nullable=True)
    hidden = db.Column(db.Boolean)
    quick_responses_allowed = db.Column(db.Boolean)
    driver_license_types = db.Column(db.JSON)
    accept_incomplete_resumes = db.Column(db.Boolean)
    employer = db.Column(db.JSON)
    published_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    initial_created_at = db.Column(db.DateTime)
    negotiations_url = db.Column(db.String, nullable=True)
    suitable_resumes_url = db.Column(db.String, nullable=True)
    apply_alternate_url = db.Column(db.String)
    has_test = db.Column(db.Boolean)
    test = db.Column(db.String, nullable=True)
    alternate_url = db.Column(db.String)
    working_days = db.Column(db.JSON)
    working_time_intervals = db.Column(db.JSON)
    working_time_modes = db.Column(db.JSON)
    accept_temporary = db.Column(db.Boolean)
    languages = db.Column(db.JSON)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class SalarySchema(Schema):
    from_salary = fields.Integer()
    to_salary = fields.Integer()
    currency = fields.String()
    gross = fields.Boolean()


class AreaSchema(Schema):
    id = fields.String()
    name = fields.String()
    url = fields.String()


class TypeSchema(Schema):
    id = fields.String()
    name = fields.String()


class AddressSchema(Schema):
    city = fields.String()
    street = fields.String()
    building = fields.String()
    lat = fields.Float()
    lng = fields.Float()
    description = fields.String(allow_none=True)
    raw = fields.String()
    metro = fields.String(allow_none=True)
    metro_stations = fields.List(fields.String())


class ExperienceSchema(Schema):
    id = fields.String()
    name = fields.String()


class ScheduleSchema(Schema):
    id = fields.String()
    name = fields.String()


class EmploymentSchema(Schema):
    id = fields.String()
    name = fields.String()


class EmployerSchema(Schema):
    id = fields.String()
    name = fields.String()
    url = fields.URL()
    vacancies_url = fields.URL()
    alternate_url = fields.URL()
    logo_urls = fields.Dict(
        keys=fields.String(), values=fields.String(), allow_none=True)
    accredited_it_employer = fields.Boolean()
    trusted = fields.Boolean()


class VacancySchema(Schema):
    id = fields.Integer()
    hh_id = fields.Integer()
    premium = fields.Boolean()
    billing_type = fields.Dict(keys=fields.String(), values=fields.String())
    relations = fields.List(fields.Dict())
    name = fields.String()
    insider_interview = fields.String(allow_none=True)
    response_letter_required = fields.Boolean()
    area = fields.Nested(AreaSchema)
    salary = fields.Nested(SalarySchema)
    type = fields.Nested(TypeSchema)
    address = fields.Nested(AddressSchema, allow_none=True)
    allow_messages = fields.Boolean()
    experience = fields.Nested(ExperienceSchema)
    schedule = fields.Nested(ScheduleSchema)
    employment = fields.Nested(EmploymentSchema)
    department = fields.String(allow_none=True)
    contacts = fields.String(allow_none=True)
    description = fields.String()
    branded_description = fields.String(allow_none=True)
    vacancy_constructor_template = fields.String(allow_none=True)
    key_skills = fields.List(fields.Dict(
        keys=fields.String(), values=fields.String()))
    accept_handicapped = fields.Boolean()
    accept_kids = fields.Boolean()
    archived = fields.Boolean()
    response_url = fields.URL(allow_none=True)
    specializations = fields.List(fields.Dict())
    professional_roles = fields.List(fields.Dict(
        keys=fields.String(), values=fields.String()))
    code = fields.String(allow_none=True)
    hidden = fields.Boolean()
    quick_responses_allowed = fields.Boolean()
    driver_license_types = fields.List(fields.String())
    accept_incomplete_resumes = fields.Boolean()
    employer = fields.Nested(EmployerSchema)
    published_at = fields.DateTime()
    created_at = fields.DateTime()
    initial_created_at = fields.DateTime()
    negotiations_url = fields.URL(allow_none=True)
    suitable_resumes_url = fields.URL(allow_none=True)
    apply_alternate_url = fields.URL()
    has_test = fields.Boolean()
    test = fields.String(allow_none=True)
    alternate_url = fields.URL()
    working_days = fields.List(fields.String())
    working_time_intervals = fields.List(fields.Dict(
        keys=fields.String(), values=fields.String()))
    working_time_modes = fields.List(fields.Dict(
        keys=fields.String(), values=fields.String()))
    accept_temporary = fields.Boolean()
    languages = fields.List(fields.String())
    added_at = fields.DateTime()
    status = fields.String()
    user_id = fields.Integer()


# class SalarySchema(Schema):
#     from_salary = fields.Integer()
#     to_salary = fields.Integer()
#     currency = fields.String()
#     gross = fields.Boolean()


# class VacancySchema(Schema):
#     id = fields.Integer()
#     name = fields.String()
#     description = fields.String()
#     salary = fields.Nested(SalarySchema)
#     date_added = fields.DateTime()
#     user_id = fields.Integer()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    vacancies = db.relationship('Vacancy', backref='user', lazy='dynamic')
    sub = db.Column(db.String)
    image = db.Column(db.String)
    # obj = db.Column(db.String)


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()
    date_created = fields.DateTime()
    vacancies = fields.List(fields.Nested(VacancySchema))
    sub = fields.String()
    image = fields.String()
    # obj = fields.List(fields.Dict())


user_schema = UserSchema()
users_schema = UserSchema(many=True)
vacancy_schema = VacancySchema()
vacancies_schema = VacancySchema(many=True)
# job_vacancies_schema = JobVacancySchema(many=True)


@app.route('/users')
def users():
    users = User.query.all()
    # response.headers['Custom-Header'] = 'Your custom value'

    response = make_response(users_schema.dump(users))
    response.headers['Content-Type'] = 'application/json; charset="utf-8"'
    response.headers['asda'] = 'test123'

    return response
    # return users_schema.dump(users)


@app.route('/users/<user_id>')
def user(user_id):
    user = User.query.filter(User.id == user_id).first()

    return user_schema.dump(user)


@app.route('/users-sub/<sub>')
def user_sub(sub):
    user = User.query.filter(User.sub == sub).first()

    return user_schema.dump(user)


@app.route('/create-user', methods=['POST'])
def create_user():
    request_data = request.get_json()

    try:
        validated_data = user_schema.load(request_data)
    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    new_user = User(image=validated_data['image'],
                    email=validated_data['email'], name=validated_data['name'], sub=validated_data['sub'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201


@app.route('/vacancies')
def vacancies():
    all_vacancies = Vacancy.query.all()

    return vacancies_schema.dump(all_vacancies)


@app.route('/vacancies/<vacancy_id>')
def vacancy(vacancy_id):
    vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first()

    return vacancy_schema.dump(vacancy)


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

    # new_vacancy = Vacancy(name=validated_data['name'], salary=validated_data['salary'],
    #                       description=validated_data['description'], user_id=validated_data['user_id'])

    new_vacancy = Vacancy(
        premium=validated_data['premium'],
        billing_type=validated_data['billing_type'],
        relations=validated_data['relations'],
        name=validated_data['name'],
        insider_interview=validated_data['insider_interview'],
        response_letter_required=validated_data['response_letter_required'],
        area=validated_data['area'],
        salary=validated_data['salary'],
        type=validated_data['type'],
        address=validated_data['address'],
        allow_messages=validated_data['allow_messages'],
        experience=validated_data['experience'],
        schedule=validated_data['schedule'],
        employment=validated_data['employment'],
        department=validated_data['department'],
        contacts=validated_data['contacts'],
        description=validated_data['description'],
        branded_description=validated_data['branded_description'],
        vacancy_constructor_template=validated_data['vacancy_constructor_template'],
        key_skills=validated_data['key_skills'],
        accept_handicapped=validated_data['accept_handicapped'],
        accept_kids=validated_data['accept_kids'],
        archived=validated_data['archived'],
        response_url=validated_data['response_url'],
        specializations=validated_data['specializations'],
        professional_roles=validated_data['professional_roles'],
        code=validated_data['code'],
        hidden=validated_data['hidden'],
        quick_responses_allowed=validated_data['quick_responses_allowed'],
        driver_license_types=validated_data['driver_license_types'],
        accept_incomplete_resumes=validated_data['accept_incomplete_resumes'],
        employer=validated_data['employer'],
        published_at=validated_data['published_at'],
        created_at=validated_data['created_at'],
        initial_created_at=validated_data['initial_created_at'],
        negotiations_url=validated_data['negotiations_url'],
        suitable_resumes_url=validated_data['suitable_resumes_url'],
        apply_alternate_url=validated_data['apply_alternate_url'],
        has_test=validated_data['has_test'],
        test=validated_data['test'],
        alternate_url=validated_data['alternate_url'],
        working_days=validated_data['working_days'],
        working_time_intervals=validated_data['working_time_intervals'],
        working_time_modes=validated_data['working_time_modes'],
        accept_temporary=validated_data['accept_temporary'],
        languages=validated_data['languages'],
        added_at=validated_data['added_at'],
        status=validated_data['status'],
        user_id=validated_data['user_id'],
        hh_id=validated_data['hh_id']
    )

    db.session.add(new_vacancy)
    db.session.commit()

    return jsonify({'message': 'Vacancy added successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
