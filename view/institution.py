from flask import Blueprint, request
from model.institution import AdministrativeCategory
from model.course import CourseModality

from controller.institution import InstitutionController
from dtos.institution import GetInstitutionRanking
from dataclasses import asdict

blueprint = Blueprint('institution', __name__, url_prefix='/instituicoes')

@blueprint.get('ranking/<int:year>/<string:category>/<string:modality>')
def get_institution_ranking(year: int, category: str, modality: str):
    category_type: AdministrativeCategory = AdministrativeCategory.parse(category)
    modality_type: CourseModality = CourseModality.parse(modality)

    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 10))

    args = GetInstitutionRanking(
        year=year,
        category=category_type,
        modality=modality_type,
        page=page,
        page_size=page_size)

    response = InstitutionController.get_institution_ranking(args)
    return [asdict(x) for x in response] 
