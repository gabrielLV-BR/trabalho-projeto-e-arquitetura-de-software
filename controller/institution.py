from peewee import fn
from playhouse.shortcuts import model_to_dict
from model.institution import Institution
from model.course import Course
from model.registration import Registration
from loggers.logger import Logging

from dtos.institution import GetInstitutionRanking, InstitutionRanking

class InstitutionController:
    def get_institution_ranking(args: GetInstitutionRanking) -> list[InstitutionRanking]:
        Logging.log(f'Searching for institutions ranking with parameters {args.year}, {args.category}, {args.modality}')

        registration_count = fn.SUM(Registration.student_count)

        institutions = (Institution
            .select(Institution.id, registration_count.alias('total_student_count'))
            .join_from(Institution, Course)
            .join_from(Course, Registration)
            .where((Registration.year == args.year) &
                (Course.modality_type == args.modality.value) &
                (Institution.category_type == args.category.value))
            .group_by(Institution.id)
            .order_by(registration_count.desc())
            .paginate(args.page, args.page_size))

        response = []
        base_index = (args.page - 1) * args.page_size + 1
        for index, ranking in enumerate(institutions):
            institution = Course.get(ranking.id)
            response.append(
                InstitutionRanking(
                    base_index + index,
                    ranking.total_student_count,
                    model_to_dict(institution)))

        return response