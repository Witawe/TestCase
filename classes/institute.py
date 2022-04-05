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

    def add_exam_marks(self, exam_result: ExamPoints):
        if type(exam_result) != ExamPoints:
            raise Exception('Type error')
        for i in self.exam_results:
            if i == exam_result:
                raise Exception('error')
        self.exam_results.append(exam_result)
