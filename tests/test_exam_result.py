from main import Student, ExamPoints
from classes.institute import Institute
from classes.getExamResult import getExamResult
import unittest

class TestAddExamResult(unittest.TestCase):
    def test_one(self): #correct
        stud = Student('Луковцев Алексей Владимирович', 185775)
        result = ExamPoints(stud, 59.9, 25.4)
        inst = Institute()
        inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 1)

    def test_two(self): #correct
        stud = Student('Луковцев Алексей Владимирович', 185775)
        result = ExamPoints(stud, 59.9, 25.4)
        result1 = ExamPoints(stud, 55.5, 30.0)
        inst = Institute()
        inst.add_exam_marks(result)
        inst.add_exam_marks(result1)
        self.assertEqual(len(inst.exam_results), 1)
'''
    def test_three(self):
        stud = Student('Луковцев Алексей Владимирович', 185775)
        result = ExamPoints(stud, 80.0, 10)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_four(self):
        stud = Student('Луковцев Алексей Владимирович', 185775)
        result = ExamPoints(stud, 60.0, 40)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_five(self):
        stud = Student('Луковцев Алексей Владимирович', 185775)
        result = ExamPoints(stud, -60.0, 40)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_six(self):
        result = ExamPoints(12, 60.0, 25)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_seven(self):
        stud = Student('', '185775')
        result = ExamPoints(stud, 60.0, 24)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_eight(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(123)
        self.assertEqual(len(inst.exam_results), 0)

    def test_nine(self):
        stud = Student('Луковцев Алексей Владимирович', 185775)
        result = ExamPoints(stud, 60.0, -25)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_ten(self):
        stud = Student('Луковцев Алексей Владимирович', 185775)
        result = ExamPoints(stud, 60, 25)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)
'''

class TestGetExamResult(unittest.TestCase):
    def test_2(self):
        g_examres = getExamResult("")
        with self.assertRaises(Exception):
            getExamResult(g_examres)

    def test_3(self):
        g_examres = getExamResult(None)
        with self.assertRaises(Exception):
            getExamResult(g_examres)

if __name__ == "__main__":
    unittest.main()