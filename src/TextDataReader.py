import json
from data_reader import DataReader  # Assuming DataReader is your base class

class JSONDataReader(DataReader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise Exception(f"File not found: {self.file_path}")
        except json.JSONDecodeError as e:
            raise Exception(f"Invalid JSON format: {e}")

    def get_student_scores(self, student_name):
        """Retrieve scores for a specific student."""
        data = self.read_data()
        if student_name in data:
            return data[student_name]
        else:
            raise Exception(f"Student '{student_name}' not found in the data.") 
