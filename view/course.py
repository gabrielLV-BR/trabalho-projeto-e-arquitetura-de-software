from flask import Blueprint, request
from model.institution import AdministrativeCategory
from model.course import CourseModality

from dtos.course import GetCourseRanking
from controller.course import CourseController

from dataclasses import asdict

blueprint = Blueprint('course', __name__, url_prefix='/cursos')

@blueprint.get('ranking/<int:year>/<string:category>/<string:modality>')
def get_course_ranking(year: int, category: str, modality: str):
    category_type: AdministrativeCategory = AdministrativeCategory.parse(category)
    modality_type: CourseModality = CourseModality.parse(modality)

    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 10))

    args = GetCourseRanking(
        year=year,
        category=category_type,
        modality=modality_type,
        page=page,
        page_size=page_size)

    response = CourseController.get_course_ranking(args)
    return [asdict(x) for x in response] 
