import unittest
from src.json_data_reader import JSONDataReader  # Import your class

class TestJSONDataReader(unittest.TestCase):
    def setUp(self):
        """Set up test data files."""
        self.valid_file = "valid_data.json"
        self.invalid_file = "invalid_data.json"
        
        # Create a valid JSON file
        with open(self.valid_file, 'w', encoding='utf-8') as file:
            file.write("""
            {
                "Иванов Иван Иванович": {
                    "математика": 67,
                    "литература": 100
                },
                "Петров Петр Петрович": {
                    "математика": 78,
                    "химия": 87
                }
            }
            """)
        
        # Create an invalid JSON file
        with open(self.invalid_file, 'w', encoding='utf-8') as file:
            file.write("Invalid JSON")

    def tearDown(self):
        """Remove test data files."""
        import os
        os.remove(self.valid_file)
        os.remove(self.invalid_file)

    def test_read_valid_data(self):
        """Test reading a valid JSON file."""
        reader = JSONDataReader(self.valid_file)
        data = reader.read_data()
        self.assertIn("Иванов Иван Иванович", data)
        self.assertEqual(data["Иванов Иван Иванович"]["математика"], 67)

    def test_read_invalid_data(self):
        """Test reading an invalid JSON file."""
        reader = JSONDataReader(self.invalid_file)
        with self.assertRaises(Exception) as context:
            reader.read_data()
        self.assertIn("Invalid JSON format", str(context.exception))

    def test_get_keys(self):
        """Test retrieving top-level keys from the JSON."""
        reader = JSONDataReader(self.valid_file)
        keys = reader.get_keys()
        self.assertIn("Иванов Иван Иванович", keys)
        self.assertIn("Петров Петр Петрович", keys)

if __name__ == "__main__":
    unittest.main()
