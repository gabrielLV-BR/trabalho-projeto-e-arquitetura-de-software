from peewee import IntegerField, ForeignKeyField, AutoField
from model.course import Course, CourseModality
from model.base import BaseModel

# RegistrationStats
# 2014
# 2015
# 2016
# 2017
# 2018
# 2019
# 2020
# 2021
# 2022

class Registration(BaseModel):
    id = AutoField(primary_key=True)
    year = IntegerField()
    student_count = IntegerField()
    course = ForeignKeyField(Course, backref='registrations')
