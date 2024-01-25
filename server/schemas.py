import datetime

from app import db
from marshmallow import Schema, fields

# class Vacancy(db.Model):
#     __tablename__ = 'vacancies'

#     id = db.Column(db.Integer, primary_key=True)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


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
    logo_urls = fields.String(allow_none=True)
    accredited_it_employer = fields.Boolean()
    trusted = fields.Boolean()


class JobVacancySchema(Schema):
    id = fields.String()
    premium = fields.Boolean()
    billing_type = fields.Dict(keys=fields.String(), values=fields.String())
    relations = fields.List(fields.Dict())
    name = fields.String()
    insider_interview = fields.String(allow_none=True)
    response_letter_required = fields.Boolean()
    area = fields.Nested(AreaSchema)
    salary = fields.Nested(SalarySchema)
    type = fields.Nested(TypeSchema)
    address = fields.Nested(AddressSchema)
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


class Vacancy(db.Model):
    id = db.Column(db.String, primary_key=True)
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
    added_at = db.Column(db.DateTime)
    status = db.Column(db.String)
