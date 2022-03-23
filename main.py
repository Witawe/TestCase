from dataclasses import dataclass
from datetime import date

@dataclass
class Student:
    fio: str
    code: int

    def __init__(self, value_fio: str, value_code: int):
        self.fio = value_fio
        self.code = value_code

@dataclass
class Specialization:
    name: str

    def __init__(self, value_name: str):
        self.name = value_name

@dataclass
class Subject:
    code: str
    name: str
    semestr: int
    hours: int
    specialization: Specialization

    def __init__(self, value_code: str, value_name: str, value_semestr: int, value_hours: int, value_specialization: Specialization):
        self.code = value_code
        self.name = value_name
        self.semestr = value_semestr
        self.hours = value_hours
        self.specialization = value_specialization


@dataclass
class Group:
    name: str
    year: int
    specialization: Specialization

    def __init__(self, value_name: str, value_year: int, value_specialization: Specialization):
        self.name = value_name
        self.year = value_year
        self.specialization = value_specialization

@dataclass
class Exam:
    subject: Subject
    examDate: date
    year: str
    lecturer_fio: str

    def __init__(self, value_subject: Subject, value_examDate: date, value_year: str, value_lectFio: str):
        self.subject = value_subject
        self.examDate = value_examDate
        self.year = value_year
        self.lecturer_fio = value_lectFio

@dataclass
class ExamPoints:
    student: Student
    inPoints: float
    examPoints: float

    def __init__(self, value_student: Student, value_inPoints: float, value_examPoints: float):
        self.student = value_student
        self.inPoints = value_inPoints
        self.examPoints = value_examPoints

