from dataclasses import dataclass
from datetime import date
import re

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
    group: Group
    year: str
    lecturer_fio: str

    def __init__(self, value_subject: Subject, value_examDate: date, value_year: str, value_lectFio: str):
        self.subject = value_subject
        self.examDate = value_examDate
        self.year = value_year
        self.lecturer_fio = value_lectFio
        self.group = None

@dataclass
class ExamPoints:
    student: Student
    inPoints: float
    examPoints: float
    exDate: date
    groupName: str
    subject: Subject

    def __init__(self, value_student: Student, value_inPoints: float,
                 value_examPoints: float, value_date: date, value_groupName: str,
                 value_subject: Subject):
        self.setStudent(value_student)
        self.setInPoints(value_inPoints)
        self.setExamPoints(value_examPoints)
        self.setExDate(value_date)
        self.setGroupName(value_groupName)
        self.setSubject(value_subject)

    def setInPoints(self, new_inPoints):
        if type(new_inPoints) != float:
            raise Exception("Ошибка типа данных")
        if 70.0 < new_inPoints:
            raise Exception("Баллы за семестр больше 70")
        if 0.0 > new_inPoints:
            raise Exception("Баллы не могут быть отрицательными")
        self.inPoints = new_inPoints

    def getInPoints(self):
        return self.inPoints

    def setExamPoints(self, new_examPoints):
        if type(new_examPoints) != float:
            raise Exception("Ошибка типа данных")
        if 30.0 < new_examPoints:
            raise Exception("Баллы за экзамен не могут быть больше 30")
        if 0.0 > new_examPoints:
            raise Exception("Баллы за экзамен не могут быть отрицательными")
        self.examPoints = new_examPoints

    def getExamPoints(self):
        return self.examPoints

    def setStudent(self, new_student):
        if type(new_student) != Student:
            raise Exception("Ошибка типа данных")
        self.student = new_student

    def getStudent(self):
        return self.student

    def setExDate(self, exDate):
        if type(exDate) != date:
            raise Exception("Ошибка типа данных")
        self.exDate = exDate

    def getExDate(self):
        return self.exDate

    def setGroupName(self, groupName):
        if type(groupName) != str:
            raise Exception("Ошибка типа данных")
        if not re.fullmatch(r'([МБ]-)?[А-Я]+-[1-9][0-9]', groupName):
            raise Exception("Ошибка в названии группы")
        self.groupName = groupName

    def getGroupName(self):
        return self.groupName

    def setSubject(self, value_subject):
        if type(value_subject) != Subject:
            raise Exception("Ошибка типа данных")
        self.subject = value_subject

    def getSubject(self):
        return self.subject

