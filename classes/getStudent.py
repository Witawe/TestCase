from main import Student
import openpyxl

def getStudent(file, studcode):
    if studcode < 0:
        raise Exception('Номер зачетки отрицательным быть не может')
    #if str(len(studcode)) != 6:
        #raise Exception('Номер зачетки должен быть шестизначным')
    if type(studcode) != int:
        raise Exception('Номер зачетки должен числовым')
    #if studcode.isnumeric():
        #raise Exception('Номер зачетки должен быть целочисленным')
    if studcode == None:
        raise Exception('Введите номер зачетки')
    subject = openpyxl.load_workbook(file)
    sheet = subject.active

    for row in range(1, sheet.max_row + 1):
        if sheet[row][1].value == studcode:
            fio = sheet[row][0].value
            code = int(sheet[row][1].value)
            return (Student(fio, code))


