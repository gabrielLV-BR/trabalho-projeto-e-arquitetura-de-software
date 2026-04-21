from model.institution import AdministrativeCategory
from model.course import Course, CourseModality
from dataclasses import dataclass
from dtos.base import PaginationArgs

@dataclass
class GetCourseRanking(PaginationArgs): 
    year: int
    category: AdministrativeCategory
    modality: CourseModality

@dataclass
class CourseRanking():
    position: int
    totalRegistrations: int
    course: Course
    