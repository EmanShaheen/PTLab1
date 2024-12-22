import json
from data_reader import DataReader  

class JSONDataReader(DataReader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_data(self):
        """Read data from a JSON file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"File not found: {self.file_path}")
        except json.JSONDecodeError as e:
            raise Exception(f"Invalid JSON format: {e}")

    def get_keys(self):
        """Return a list of top-level keys in the JSON."""
        data = self.read_data()
        return list(data.keys())
