"""

Project #1 
Name: Don Nakashima

Comments:
Not sure how to make the parsing more efficient, but works as intended.

Sources:
https://docs.python.org/3/library/xml.etree.elementtree.html - Referenced for tree builder

"""
import csv
import json
import xml.etree.ElementTree as ET

def read_csv_string(input_):
    """
    Takes a string which is the contents of a CSV file.
    Returns an object containing the data from the file.
    The specific representation of the object is up to you.
    The data object will be passed to the write_*_string functions.
    """
    
    lines = input_.split('\n')
    header = lines[0].split(',')
    
    len_header = len(header)
    len_rows = len(lines) - 1

    counter = 1
    total_data = []
    while counter < len_rows:
        d = {}
        
        row = lines[counter].split(',')
        for i in range(len_header):
            d[header[i]] = row[i]
            
        total_data.append(d)
        counter += 1
    
    return total_data

def read_json_string(input_):
    """
    Similar to read_csv_string, except works for JSON files.
    """
    return json.loads(input_)

def read_xml_string(input_):
    """
    Reads XML string and converts to a readable format.
    """
    
    total_data = []
    
    data = ET.fromstring(input_)
    for record in data:
        d = {}
        for child in record:
            d[str(child.tag)] = str(child.text)
        total_data.append(d)
            
    return total_data

def write_csv_string(data):
    """
    Takes a data object (created by one of the read_*_string functions).
    Returns a string in the CSV format.
    """

    multiline = ""
    
    counter = 0
    for d in data:
        key = ""
        value = ""
        for k, v in d.items():
            key += (str(k) + ",")
            value += (str(v) + ",")
            
        key = key[:-1]
        value = value[:-1]
        if counter == 0:
            multiline += key + '\n'
            multiline += value + '\n'
        else:
            multiline += value + '\n'
        
        counter += 1
    
    return multiline

def write_json_string(data):
    """
    Writes JSON strings. Similar to write_csv_string.
    """
    return json.dumps(data)
    

def write_xml_string(data):
    """
    Writes XML string.
    """
    tree = ET.TreeBuilder()
    tree.start("data", {})
    
    for d in data:
        tree.start("record", {})
        
        for k, v in d.items():
            tree.start(str(k))
            tree.data(str(v))
            tree.end(str(k))
        
        tree.end("record")
    tree.end("data")
    
    root = tree.close()
    
    return ET.tostring(root).decode("utf-8")



# Default Test
# More testing is done in tests.py
if __name__ == "__main__":
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
