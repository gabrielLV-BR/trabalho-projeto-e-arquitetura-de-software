# Course
# Nome do Curso
# Nome Detalhado do Curso
# Modalidade
# Grau

from enum import Enum
from peewee import TextField, IntegerField, ForeignKeyField, PrimaryKeyField
from model.base import BaseModel
from model.institution import Institution

class CourseModality(Enum):
    PRESENTIAL = 1
    EAD = 2

    def parse(modality: str):
        modality = modality.strip().lower()

        match modality:
            case 'presential' | 'presencial':
                return CourseModality.PRESENTIAL
            case 'ead':
                return CourseModality.EAD
        
        raise ValueError('Invalid modality specified')
        

class Course(BaseModel):
    id = PrimaryKeyField()
    name = TextField(index=True)
    detailed_name = TextField()
    modality = TextField()
    modality_type = IntegerField(index=True)
    degree = TextField()
    institution = ForeignKeyField(Institution, backref='courses')
