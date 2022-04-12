from main import *

class Institute:
    def __init__(self):
        self.students = []
        self.groups = []
        self.subjects = []
        self.specs = []
        self.exams = []
        self.exam_results = []

    def add_spec(self, spec: Specialization):
        if type(spec) != Specialization:
            raise Exception('Type error')
        for i in self.specs:
            if i == spec:
                raise Exception('error')
        self.specs.append(spec)

    def add_stud(self, stud: Student):
        if type(stud) != Student:
            raise Exception('Type error')
        for i in self.students:
            if i == stud:
                raise Exception('error')
        self.students.append(stud)

    def add_group(self, group: Group):
        if type(group) != Group:
            raise Exception('Type error')
        for i in self.groups:
            if i == group:
                raise Exception('error')
        self.groups.append(group)

    def add_subject(self, subject: Subject):
        if type(subject) != Subject:
            raise Exception('Type error')
        for i in self.subjects:
            if i == subject:
                raise Exception('error')
        self.subjects.append(subject)

    def add_exam(self, exam: Exam):
        if type(exam) != Exam:
            raise Exception('Type error')
        for i in self.exams:
            if i == exam:
                raise Exception('error')
        self.exams.append(exam)

    def add_exam_result(self, exam_results):
        t = (exam_results.exam.group.name, exam_results.exam.subject.name, exam_results.examDate)
        if t in self.exam_results.keys():
            self.exam_results[(exam_results.exam.group.name, exam_results.exam.subject.name, exam_results.examDate)].append(
                exam_results)
        else:
            self.exam_results[(exam_results.exam.group.name, exam_results.exam.subject.name, exam_results.examDate)] = [
                exam_results]

    def get_student(self, studCode: int):
        if studCode < 0:
            raise Exception('Номер зачетки отрицательным быть не может')
        if len(str(studCode)) != 6:
            raise Exception('Номер зачетки должен быть шестизначным')
        if type(studCode) != int:
            raise Exception('Номер зачетки должен числовым')
        if studCode == None:
            raise Exception('Введите номер зачетки')
        for student in self.students:
            if student.code == studCode:
                return student
            else:
                raise Exception('Студент не найден')

    def get_subject(self, sub_name: str):
        for subject in self.subjects:
            if subject.name == sub_name:
                return subject
            else:
                raise Exception('Предмет не найден')

    def get_spec(self, name: str):
        for spec in self.specs:
            if spec.name == name:
                return spec
            else:
                raise Exception('Специализация не найдена')

    def get_group(self, name: str):
        for group in self.groups:
            if group.name == name:
                return group
            else:
                raise Exception('Группа не найдена')

    def get_exam(self, gr_name, subj_name, exam_date):
        pass

    def get_exam_result(self, group_name, subject_name, date):
        return self.exam_points[(group_name, subject_name, date)]
