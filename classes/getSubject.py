from main import Subject, Specialization
import openpyxl

def getSubject(file, name_sub):
    #file = "./data/2семестр.xlsx"
    subject = openpyxl.load_workbook(file)
    sheet = subject.active
    #name_sub = "Иностранный язык в научной сфере"
    #subjects = list()

    for row in range(1, sheet.max_row):
        if sheet[row][1].value == name_sub:
            code = sheet[row][0].value
            name = sheet[row][1].value
            semestr = int(sheet[row][2].value)
            hours = int(sheet[row][3].value)
            specialization = Specialization(sheet[row][4].value)
            return (Subject(code, name, semestr, hours, specialization))

#print(getSubject("../data/2семестр.xlsx", "Иностранный язык в научной сфере"))