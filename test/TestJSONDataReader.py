import unittest
from json_data_reader import JSONDataReader

class TestJSONDataReader(unittest.TestCase):
    def setUp(self):
        # Create a sample JSON file for testing
        self.test_file = "test_data.json"
        self.invalid_file = "invalid_data.json"
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("""
            {
                "Иванов Иван Иванович": {
                    "математика": 67,
                    "литература": 100,
                    "программирование": 91
                },
                "Петров Петр Петрович": {
                    "математика": 78,
                    "химия": 87,
                    "социология": 61
                }
            }
            """)
        with open(self.invalid_file, 'w', encoding='utf-8') as file:
            file.write("Invalid JSON Content")

    def tearDown(self):
        import os
        os.remove(self.test_file)
        os.remove(self.invalid_file)

    def test_read_data_valid_file(self):
        reader = JSONDataReader(self.test_file)
        data = reader.read_data()
        self.assertIn("Иванов Иван Иванович", data)
        self.assertIn("Петров Петр Петрович", data)

    def test_read_data_invalid_file(self):
        reader = JSONDataReader(self.invalid_file)
        with self.assertRaises(Exception) as context:
            reader.read_data()
        self.assertIn("Invalid JSON format", str(context.exception))

    def test_get_student_scores_valid(self):
        reader = JSONDataReader(self.test_file)
        scores = reader.get_student_scores("Иванов Иван Иванович")
        self.assertEqual(scores["математика"], 67)

    def test_get_student_scores_missing(self):
        reader = JSONDataReader(self.test_file)
        with self.assertRaises(Exception) as context:
            reader.get_student_scores("Сидоров Сидор Сидорович")
        self.assertIn("Student 'Сидоров Сидор Сидорович' not found", str(context.exception))
