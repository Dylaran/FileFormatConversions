import unittest
from file_format_conversion import *

class TestMethods(unittest.TestCase):
    # Test 1
    def test_CSV_to_CSV(self):
        input_ = """
        col1,col2,col3
        1,2,3
        4,5,6
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        print("CSV Input:")
        print(input_)
        print()
        data = read_csv_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_csv_string(data)
        output = super_strip(output)
        print("CSV Output:")
        print(output)
        print()
        self.assertEqual(input_, output)

    # Test 2
    def test_JSON_to_JSON(self):
        input_ = """
        [{"col1": "1", "col2": "2", "col3": "3"}, {"col1": "4", "col2": "5", "col3": "6"}]
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        print("JSON Input:")
        print(input_)
        print()
        data = read_json_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_json_string(data)
        output = super_strip(output)
        print("JSON Output:")
        print(output)
        print()
        self.assertEqual(input_, output)

    # Test 3
    def test_XML_to_XML(self):
        input_ = """
        <data><record><col1>1</col1><col2>2</col2><col3>3</col3></record><record><col1>4</col1><col2>5</col2><col3>6</col3></record></data>
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        print("XML Input:")
        print(input_)
        print()
        data = read_xml_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_xml_string(data)
        output = super_strip(output)
        print("XML Output:")
        print(output)
        print()
        self.assertEqual(input_, output)

    # Test 4
    def test_CSV_to_JSON(self):
        input_ = """
        col1,col2,col3
        1,2,3
        4,5,6
        """
        expected = """
        [{"col1": "1", "col2": "2", "col3": "3"}, {"col1": "4", "col2": "5", "col3": "6"}]
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        expected = super_strip(expected)
        print("Input:")
        print(input_)
        print()
        data = read_csv_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_json_string(data)
        output = super_strip(output)
        print("Output:")
        print(output)
        print()
        self.assertEqual(expected, output)

    # Test 5
    def test_CSV_to_XML(self):
        input_ = """
        col1,col2,col3
        1,2,3
        4,5,6
        """
        expected = """
        <data><record><col1>1</col1><col2>2</col2><col3>3</col3></record><record><col1>4</col1><col2>5</col2><col3>6</col3></record></data>
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        expected = super_strip(expected)
        print("Input:")
        print(input_)
        print()
        data = read_csv_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_xml_string(data)
        output = super_strip(output)
        print("Output:")
        print(output)
        print()
        self.assertEqual(expected, output)

    # Test 6
    def test_JSON_to_CSV(self):
        input_ = """
        [{"col1": "1", "col2": "2", "col3": "3"}, {"col1": "4", "col2": "5", "col3": "6"}]
        """
        expected = """
        col1,col2,col3
        1,2,3
        4,5,6
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        expected = super_strip(expected)
        print("Input:")
        print(input_)
        print()
        data = read_json_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_csv_string(data)
        output = super_strip(output)
        print("Output:")
        print(output)
        print()
        self.assertEqual(expected, output)

    # Test 7
    def test_JSON_to_XML(self):
        input_ = """
        [{"col1": "1", "col2": "2", "col3": "3"}, {"col1": "4", "col2": "5", "col3": "6"}]
        """
        expected = """
        <data><record><col1>1</col1><col2>2</col2><col3>3</col3></record><record><col1>4</col1><col2>5</col2><col3>6</col3></record></data>
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        expected = super_strip(expected)
        print("Input:")
        print(input_)
        print()
        data = read_json_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_xml_string(data)
        output = super_strip(output)
        print("Output:")
        print(output)
        print()
        self.assertEqual(expected, output)

    # Test 8
    def test_XML_to_CSV(self):
        input_ = """
        <data><record><col1>1</col1><col2>2</col2><col3>3</col3></record><record><col1>4</col1><col2>5</col2><col3>6</col3></record></data>
        """
        expected = """
        col1,col2,col3
        1,2,3
        4,5,6
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        expected = super_strip(expected)
        print("Input:")
        print(input_)
        print()
        data = read_xml_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_csv_string(data)
        output = super_strip(output)
        print("Output:")
        print(output)
        print()
        self.assertEqual(expected, output)
    
    # Test 9
    def test_XML_to_JSON(self):
        input_ = """
        <data><record><col1>1</col1><col2>2</col2><col3>3</col3></record><record><col1>4</col1><col2>5</col2><col3>6</col3></record></data>
        """
        expected = """
        [{"col1": "1", "col2": "2", "col3": "3"}, {"col1": "4", "col2": "5", "col3": "6"}]
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        input_ = super_strip(input_)
        expected = super_strip(expected)
        print("Input:")
        print(input_)
        print()
        data = read_xml_string(input_)
        print("Your data object:")
        print(data)
        print()
        output = write_json_string(data)
        output = super_strip(output)
        print("Output:")
        print(output)
        print()
        self.assertEqual(expected, output)

    # Test 10
    def test_All(self):
        csv_ = """
        col1,col2,col3
        1,2,3
        4,5,6
        """
        json_ = """
        [{"col1": "1", "col2": "2", "col3": "3"}, {"col1": "4", "col2": "5", "col3": "6"}]
        """
        xml_ = """
        <data><record><col1>1</col1><col2>2</col2><col3>3</col3></record><record><col1>4</col1><col2>5</col2><col3>6</col3></record></data>
        """
        def super_strip(input_):
            """
            Removes all leading/trailing whitespace and blank lines
            """
            lines = []
            for line in input_.splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
            return "\n".join(lines) + "\n"
        csv_ = super_strip(csv_)
        json_ = super_strip(json_)
        xml_ = super_strip(xml_)
        data_csv = read_csv_string(csv_)
        data_json = read_json_string(json_)
        data_xml = read_xml_string(xml_)
        self.assertEqual(csv_, super_strip(write_csv_string(data_csv)))
        self.assertEqual(csv_, super_strip(write_csv_string(data_json)))
        self.assertEqual(csv_, super_strip(write_csv_string(data_xml)))
        self.assertEqual(json_, super_strip(write_json_string(data_csv)))
        self.assertEqual(json_, super_strip(write_json_string(data_json)))
        self.assertEqual(json_, super_strip(write_json_string(data_xml)))
        self.assertEqual(xml_, super_strip(write_xml_string(data_csv)))
        self.assertEqual(xml_, super_strip(write_xml_string(data_json)))
        self.assertEqual(xml_, super_strip(write_xml_string(data_xml)))

    
if __name__ == "__main__":
    unittest.main()