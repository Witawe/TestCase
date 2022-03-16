from main import Student, Specialization, Subject, Group, Exam, ExamPoints
from datetime import date
import unittest

class TestClasses(unittest.TestCase):
    """-----------Class Student-----------"""
    def test_class_student_1(self):
        student = Student("Луковцев Алексей Владимирович", 185775)
        self.assertEqual("Луковцев Алексей Владимирович", student.fio)
        self.assertEqual(185775, student.code)

    def test_class_student_2(self):
        student = Student("185775", 185775)
        self.assertEqual("185775", student.fio)
        self.assertEqual(185775, student.code)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_student_3(self):
        student = Student("Луковцев Алексей Владимирович", "стосколькотосколько")
        self.assertEqual("Луковцев Алексей Владимирович", student.fio)
        self.assertEqual("asdlaksd", student.code)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_student_4(self):
        student = Student("185775", "Луковцев Алексей Владимирович")
        self.assertEqual("185775", student.fio)
        self.assertEqual("Луковцев Алексей Владимирович", student.code)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_student_5(self):
        student = Student("", 185775)
        self.assertEqual("", student.fio)
        self.assertEqual(185775, student.code)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_student_6(self):
        student = Student("ЛуковцевАлексейВладимирович", 185775)
        self.assertEqual("ЛуковцевАлексейВладимирович", student.fio)
        self.assertEqual(185775, student.code)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_student_7(self):
        student = Student("ЛуковцевАлексейВладимирович", "")
        self.assertEqual("ЛуковцевАлексейВладимирович", student.fio)
        self.assertEqual("", student.code)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    """-----------Class Specialization-----------"""
    def test_class_specialization_1(self):
        spec = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", spec.name)

    def test_class_specialization_2(self):
        spec = Specialization("")
        self.assertEqual("", spec.name)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_specialization_3(self):
        spec = Specialization("12312312")
        self.assertEqual("12312312", spec.name)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    """-----------Class Subject-----------"""
    def test_class_subject_1(self):
        #specialization = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, Specialization)
        self.assertEqual("Б1.В.02", subject.code)
        self.assertEqual("Методы тестирования и верификации программных продуктов", subject.name)
        self.assertEqual(2, subject.semestr)
        self.assertEqual(108, subject.hours)
        self.assertEqual(Specialization, subject.specialization)

    def test_class_subject_2(self):
        #specialization = Specialization("ФИИТ")
        subject = Subject("", "", 0, 0, Specialization)
        self.assertEqual("", subject.code)
        self.assertEqual("", subject.name)
        self.assertEqual(0, subject.semestr)
        self.assertEqual(0, subject.hours)
        self.assertEqual(Specialization, subject.specialization)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_subject_3(self):
        #specialization = Specialization("ФИИТ")
        subject = Subject("123223123", "123123123", "first", "onehundred", Specialization)
        self.assertEqual("123223123", subject.code)
        self.assertEqual("123123123", subject.name)
        self.assertEqual("first", subject.semestr)
        self.assertEqual("onehundred", subject.hours)
        self.assertEqual(Specialization, subject.specialization)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    """-----------Class Group-----------"""
    def test_class_group_1(self):
        specialization = "ФИИТ"
        group = Group("М-ФИИТ-21", 2021, specialization)
        self.assertEqual("М-ФИИТ-21", group.name)
        self.assertEqual(2021, group.year)
        self.assertEqual(specialization, group.specialization)

    def test_class_group_2(self):
        specialization = "М-ФИИТ-21"
        group = Group("", 0, specialization)
        self.assertEqual("", group.name)
        self.assertEqual(0, group.year)
        self.assertEqual(specialization, group.specialization)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_group_3(self):
        specialization = "М-ФИИТ-21"
        group = Group("asdasdasdasd", 0, specialization)
        self.assertEqual("asdasdasdasd", group.name)
        self.assertEqual(0, group.year)
        self.assertEqual(specialization, group.specialization)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    """-----------Class Exam-----------"""
    def test_class_exam_1(self):
        data = date(2021, 1, 1)
        exam = Exam(Subject, data, 2021, "Эверстов Владимир Васильевич")
        self.assertEqual(Subject ,exam.subject)
        self.assertEqual(data, exam.examDate)
        self.assertEqual(2021, exam.year)
        self.assertEqual("Эверстов Владимир Васильевич", exam.lecturer_fio)

    def test_class_exam_2(self):
        data = date(0, 0, 0)
        exam = Exam(Subject, data, 0, "")
        self.assertEqual(Subject, exam.subject)
        self.assertEqual(data, exam.examDate)
        self.assertEqual(0, exam.year)
        self.assertEqual("", exam.lecturer_fio)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_exam_3(self):
        data = date(2030, 1, 1)
        exam = Exam(Subject, data, 2021, "ЭверстовВладимирВасильевич")
        self.assertEqual(Subject ,exam.subject)
        self.assertEqual(data, exam.examDate)
        self.assertEqual(2021, exam.year)
        self.assertEqual("ЭверстовВладимирВасильевич", exam.lecturer_fio)
        with self.assertRaises(Exception):
            print("oshibka oshibka")


    def test_class_exam_4(self):
        data = date(2021, 1, 1)
        exam = Exam(Subject, data, 2021, "фдвлыол фывлолдф фывфжылвд")
        self.assertEqual(Subject ,exam.subject)
        self.assertEqual(data, exam.examDate)
        self.assertEqual(2021, exam.year)
        self.assertEqual("фдвлыол фывлолдф фывфжылвд", exam.lecturer_fio)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    """-----------Class ExamPoints-----------"""
    def test_class_exampoints_1(self):
        exampoints = ExamPoints(Student, 59.9, 30)
        self.assertEqual(Student, exampoints.student)
        self.assertEqual(64.9, exampoints.inPoints)
        self.assertEqual(30, exampoints.examPoints)

    def test_class_exampoints_2(self):
        exampoints = ExamPoints(Student, 108, 30)
        self.assertEqual(Student, exampoints.student)
        self.assertEqual(108, exampoints.inPoints)
        self.assertEqual(30, exampoints.examPoints)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

    def test_class_exampoints_3(self):
        exampoints = ExamPoints(Student, -60, 30)
        self.assertEqual(Student, exampoints.student)
        self.assertEqual(-60, exampoints.inPoints)
        self.assertEqual(30, exampoints.examPoints)
        with self.assertRaises(Exception):
            print("oshibka oshibka")

if __name__ == '__main__':
    unittest.main()