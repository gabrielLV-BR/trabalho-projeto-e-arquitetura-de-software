from model.course import Course, CourseModality
from model.registration import Registration
from loggers.logger import Logging
from dtos.student import GetTotalStudents, TotalStudents

class StudentController:
    def get_total_students(args: GetTotalStudents) -> TotalStudents:
        Logging.log(f'Searching for users ranking on year {args.year}')

        query = (Registration
            .select(Registration, Course)
            .join(Course)
            .where(Registration.year == args.year))

        presential_students =\
            (query
                .where(
                (Registration
                    .course
                    .modality_type == CourseModality.PRESENTIAL.value))
                .count())
        
        ead_students =\
            (query
                .where(
                (Registration
                    .course
                    .modality_type == CourseModality.EAD.value))
                .count())
        
        return TotalStudents(
            totalStudentsPresential=presential_students,
            totalStudentsEAD=ead_students,
            totalStudents=presential_students + ead_students)