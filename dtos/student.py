from dataclasses import dataclass

@dataclass
class GetTotalStudents: 
    year: int

@dataclass
class TotalStudents():
    totalStudentsPresential: int
    totalStudentsEAD: int
    totalStudents: int