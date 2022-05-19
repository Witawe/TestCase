from main import *
import datetime

class Institute:
    def __init__(self):
        self.students = []
        self.groups = []
        self.subjects = []
        self.specs = []
        self.exams = []
        self.exam_points = []

    def add_spec(self, spec: Specialization):
        if type(spec) != Specialization:
            raise Exception('Ошибка типа')
        if len(str(spec)) <= 1:
            raise Exception("Введите название корректно")
        for i in self.specs:
            if i == spec:
                raise Exception('Эта специализация уже существует')
        self.specs.append(spec)

    def add_stud(self, stud: Student):
        if type(stud) != Student:
            raise Exception('Ошибка типа')
        if type(stud.fio) != str or type(stud.code) != int:
            raise Exception('Ошибка типа данных')
        if len(str(stud.fio)) <= 1:
            raise Exception('Введите ФИО корректно')
        if stud.code < 0:
            raise Exception('Номер зачетки отрицательным быть не может')
        if len(str(stud.code)) != 6:
            raise Exception('Номер зачетки должен быть шестизначным')
        if stud.code == None or stud.fio == None:
            raise Exception('Введите номер зачетки')
        for i in self.students:
            if i == stud.fio:
                raise Exception('Такой студент уже существует')
            if i == stud.code:
                raise Exception('Такой студент уже существует')
        self.students.append(stud)

    def add_group(self, group: Group):
        now = datetime.datetime.now()
        stroka = group.name.split()
        if stroka[0][0] != 'Б' and stroka[0][0] != 'М':
            if stroka[0][0] != 'Б' and (now.year - group.year) >= 4:
                raise Exception('Бакалавры учатся 4 года')
            if stroka[0][0] != 'М' and (now.year - group.year) >= 2:
                raise Exception('Бакалавры учатся 2 года')
            raise Exception('Бакалавры или Магистранты?')
        if type(group.name) != str or type(group.year) != int or type(group.specialization) != Specialization:
            raise Exception('Ошибка типа данных')
        if group.specialization == '':
            raise Exception('Введите специализацию')
        if type(group) != Group:
            raise Exception('Ошибка типа')
        for i in self.groups:
            if i == group:
                raise Exception('Такая группа уже существует')
        self.groups.append(group)

    def add_subject(self, subject: Subject):
        if type(subject) != Subject:
            raise Exception('Ошибка типа')
        if type(subject.name) != str or \
                type(subject.code) != str or \
                type(subject.specialization) != Specialization or \
                type(subject.hours) != int or \
                type(subject.semestr) != int:
            raise Exception('Ошибка типа данных')
        # if subject.specialization.name == "":
        #     raise Exception('Введите специлизацию')
        if len(str(subject.specialization.name)) == 0:
            raise Exception('Введите специализацию')
        if subject.semestr == 0 or subject.hours == 0:
            raise Exception('Введите часы или семестр')
        if subject == None:
            raise Exception('Ошибка')
        for i in self.subjects:
            if i == subject:
                raise Exception('Такой предмет уже существует')
        self.subjects.append(subject)

    def add_exam(self, exam: Exam):
        now = datetime.datetime.now()
        if type(exam) != Exam:
            raise Exception('Ошибка типа')
        if type(exam.subject.name) != str or \
                type(exam.subject.code) != str or \
                type(exam.subject.specialization) != Specialization or \
                type(exam.subject.hours) != int or \
                type(exam.subject.semestr) != int:
            raise Exception('Ошибка типа данных')
        if str(exam.subject.name) == "" or \
                str(exam.subject.code) == "" or \
                str(exam.subject.specialization.name) == "" or \
                str(exam.subject.hours) == "" or \
                str(exam.subject.semestr) == "":
            raise Exception('Ошибка типа данных')
        if exam.examDate.year > now.year:
            raise Exception('Год не может быть больше текущего года')
        if str(exam.subject.specialization) == '':
            raise Exception('Введите специализацию')
        if exam.subject.semestr == 0 or exam.subject.hours == 0:
            raise Exception('Введите часы или семестр')
        if exam.lecturer_fio == "":
            raise Exception('Введите ФИО преподователя')
        if exam.year == "":
            raise Exception('Введите год сдачи экзамена')
        if exam.subject == None:
            raise Exception('Ошибка')
        for i in self.exams:
            if i == exam:
                raise Exception('Такой экзамен уже существует')
        self.exams.append(exam)

    def add_exam_points(self, exam_points: ExamPoints):
        if type(exam_points) != ExamPoints:
            raise Exception("Ошибка типа данных")
        self.exam_points.append(exam_points)

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
        if type(sub_name) != str:
            raise Exception('Ошибка типа данных')
        if str(sub_name) == "":
            raise Exception('Заполните поле')
        if str(sub_name) == None:
            raise Exception('Заполните поле')
        if str(sub_name) == None:
            raise Exception('Заполните поле')
        for subject in self.subjects:
            if subject.name == sub_name:
                return subject
            else:
                raise Exception('Предмет не найден')

    def get_spec(self, name: str):
        if type(name) != str:
            raise Exception('Ошибка типа данных')
        if str(name) == "":
            raise Exception('Заполните поле')
        if str(name) == None:
            raise Exception('Заполните поле')
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
        if type(gr_name) != str or type(subj_name) != str:
            raise Exception("Ошибка типа данных")
        if type(exam_date) != date:
            raise Exception("Ошибка формата даты")
        listExam = list()
        for exam in self.exams:
            if exam.group.name == gr_name and exam.subject.name == subj_name and exam.examDate == exam_date:
                listExam.append(exam)
        if len(listExam) == 0:
            raise Exception("Экзамен не найден")
        return listExam

    def get_exam_points(self, gr_name, subj_name, ex_date):
        if type(gr_name) != str or type(subj_name) != str:
            raise Exception("Ошибка типа данных")
        if type(ex_date) != date:
            raise Exception("Ошибка типа данных")
        listExamPoint = list()
        for exampoint in self.exam_points:
            if exampoint.groupName == gr_name and exampoint.subject.name == subj_name and exampoint.exDate == ex_date:
                listExamPoint.append(exampoint)
        if len(listExamPoint) == 0:
            raise Exception("Группа не найдена")
        return listExamPoint

