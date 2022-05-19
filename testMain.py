import unittest
from unittest.mock import patch
from io import StringIO
from addspec import main


class TestMain(unittest.TestCase):

    spec = ['Фундаментальная информатика и информационные технологии']

    @patch('builtins.input', side_effect=spec)
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_output, mock_input):
        main()
        self.assertEqual(mock_output.getvalue(), 'Фундаментальная информатика и информационные технологии\n')

    def test_2(self):
        spec1 = ['']
        with patch('builtins.input', side_effect=spec1):
            with self.assertRaises(Exception):
                main()

if __name__ == '__main__':
    unittest.main()