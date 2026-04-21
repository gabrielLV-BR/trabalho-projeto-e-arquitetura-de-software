from flask import Blueprint
from dataclasses import asdict

from controller.student import StudentController
from dtos.student import GetTotalStudents

blueprint = Blueprint('student', __name__, url_prefix='/alunos')

@blueprint.get('total/<int:year>')
def get_total_students(year: int):
    args = GetTotalStudents(year)

    response = StudentController.get_total_students(args)
    return asdict(response)
    
