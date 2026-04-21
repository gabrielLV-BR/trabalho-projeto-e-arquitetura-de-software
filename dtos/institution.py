from model.institution import Institution, AdministrativeCategory
from model.course import CourseModality
from dataclasses import dataclass
from dtos.base import PaginationArgs

@dataclass
class GetInstitutionRanking(PaginationArgs): 
    year: int
    category: AdministrativeCategory
    modality: CourseModality

@dataclass
class InstitutionRanking():
    position: int
    totalStudents: int
    institution: Institution
    