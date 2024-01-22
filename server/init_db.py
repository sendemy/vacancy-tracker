from datetime import datetime
from json import dumps

from app import User, Vacancy, app, db

app.app_context().push()
db.drop_all()

# user1 = User(email='xsfdsds@smth.com', obj=str({
#     'value': 1231
# }))
# user2 = User(email='uesr2user2@smth.com', obj=str({
#     'value': 24142
# }))
# user3 = User(email='eeheheh_third_one@smth.com', obj=str({
#     'value': 123412412412411
# }))

user1 = User(email='xsfdsds@smth.com',
             obj=dumps({'name': 'John Doe', 'email': 'john@example.com'}))
user2 = User(email='uesr2user2@smth.com',
             obj=dumps({'name': 'John Doe', 'email': 'john@example.com'}))
user3 = User(email='eeheheh_third_one@smth.com',
             obj=dumps({'name': 'John Doe', 'email': 'john@example.com'}))

vacancy1 = Vacancy(text='first vacancy text 123', user=user1)
vacancy2 = Vacancy(text='second one', user=user2)
vacancy3 = Vacancy(text='third text okay cool', user=user2)

db.create_all()
db.session.add_all([user1, user2, user3, vacancy1, vacancy2, vacancy3])
db.session.commit()
