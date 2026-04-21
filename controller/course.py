from peewee import fn
from playhouse.shortcuts import model_to_dict
from model.institution import Institution
from model.course import Course
from model.registration import Registration
from loggers.logger import Logging

from dtos.course import GetCourseRanking, CourseRanking

class CourseController:
    def get_course_ranking(args: GetCourseRanking) -> list[CourseRanking]:
        Logging.log(f'Searching for course ranking with parameters {args.year}, {args.category}, {args.modality}')

        registration_count = fn.SUM(Registration.student_count)

        courses = (Course
            .select(Course.id, registration_count.alias('total_student_count'))
            .join_from(Course, Registration)
            .join_from(Course, Institution)
            .where((Registration.year == args.year) &
                (Course.modality_type == args.modality.value) &
                (Institution.category_type == args.category.value))
            .group_by(Course.id)
            .order_by(registration_count.desc())
            .paginate(args.page, args.page_size))

        response = []
        base_index = (args.page - 1) * args.page_size + 1
        for index, ranking in enumerate(courses):
            course = Course.get(ranking.id)
            response.append(
                CourseRanking(
                    base_index + index,
                    ranking.total_student_count,
                    model_to_dict(course)))

        return response