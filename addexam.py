from classes.institute import *
import datetime

def addexam(institute):
    inst = Institute()
    sub_code = input("Введите код предмета: ")
    sub_name = input("Введите имя предмета: ")
    sub_semestr = int(input("Введите семестр: "))
    sub_hours = int(input("Общее кол-во часов: "))
    sub_specialization = Specialization(input("Специализация: "))
    data = datetime.datetime.strptime(input("Введите число сдачи экзамена (дд/мм/гггг): "), "%d/%m/%Y").date()
    examDate = input("Год сдачи экзамена: ")
    lecturer_fio = input("Введите имя преподователя: ")
    exam = Exam(Subject(sub_code, sub_name, sub_semestr, sub_hours, sub_specialization), data, examDate, lecturer_fio)
    inst.add_exam(exam)
    if (len(inst.exams)) == 1:
        print(inst.exams[-1])
        print("Экзамен успешно добавлен")
    else:
        Exception("Ошибка добавления экзамена")