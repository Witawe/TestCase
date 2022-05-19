from classes.institute import *
import sys

class main():
    inst = Institute()
    #print("Введите имя")
    #print("Пример: Луковцев Алексей Владимирович")
    if len(sys.argv) < 5:
        print('Ошибка: example - addstudent.py Луковцев Алексей Владимирович 185775')
        quit()
    fio = ''
    k = 0
    for i in sys.argv[1:4]:
        k = k + 1
        fio = fio + i
        if k <= 2:
            fio = fio + " "
    studcode = sys.argv[4]
    inst.add_stud(Student(str(fio), int(studcode)))
    if (len(inst.students)) == 1:
        print(inst.students[-1])
        print("Студент успешно добавлен")
    else:
        Exception("Ошибка добавления студента")
