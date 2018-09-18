"""
Use the JSON module to dump simple Python data structures 
Also known as: JavaScript Object Notation
"""

import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'text_files/numbers.json'
with open(filename, 'w') as f_obj:
    # this writes the list of numbers to the file
    json.dump(numbers, f_obj)