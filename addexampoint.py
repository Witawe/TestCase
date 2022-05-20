from classes.institute import *

def addexampoint(institute):
    inst = Institute()
    stud_fio = input("ФИО: ")
    stuf_code = int(input("Номер студки: "))
    inPoints = float(input("Введите балл за семестр: "))
    examPoints = float(input("Введите балл за экзамен: "))
    data = datetime.datetime.strptime(input("Введите число сдачи экзамена (дд/мм/гггг): "), "%d/%m/%Y").date()
    gr_name = input("Введите название группы: ")
    sub_code = input("Введите код предмета: ")
    sub_name = input("Введите имя предмета: ")
    sub_semestr = int(input("Введите семестр: "))
    sub_hours = int(input("Общее кол-во часов: "))
    sub_specialization = Specialization(input("Специализация: "))
    stud = Student(stud_fio, stuf_code)
    subj = Subject(sub_code, sub_name, sub_semestr, sub_hours, sub_specialization)
    exam_point = ExamPoints(stud, inPoints, examPoints, data, gr_name, subj)
    inst.add_exam_points(exam_point)
    if (len(inst.exam_points)) == 1:
        print(inst.exam_points[-1])
        print("Результат успешно добавлен")
    else:
        Exception("Ошибка добавления результатов экзамена")