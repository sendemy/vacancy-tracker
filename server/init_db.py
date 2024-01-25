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

user1 = User(email='xsfdsds@smth.com', name='John doe',
             sub='142415125125', image='sada')
user2 = User(email='uesr2user2@smth.com', name='John 2',
             sub='12121212', image='sada')
user3 = User(email='eeheheh_third_one@smth.com',
             name='Someone third heh', sub='999999', image='sada')

# vacancy1 = Vacancy(name='js frontend',
#                    description='first vacancy description 123', user=user1)
# vacancy2 = Vacancy(name='js frontend', salary={
#                    'from_salary': 10000, 'to_salary': 414142, 'currency': 'RUB', 'gross': True}, description='second one', user=user2)
# vacancy3 = Vacancy(name='js frontend', salary={'from_salary': 10000, 'to_salary': 414142,
#                    'currency': 'RUB', 'gross': True}, description='third description okay cool', user=user2)

db.create_all()
# db.session.add_all([user1, user2, user3, vacancy1, vacancy2, vacancy3])
db.session.add_all([user1, user2, user3])
db.session.commit()
