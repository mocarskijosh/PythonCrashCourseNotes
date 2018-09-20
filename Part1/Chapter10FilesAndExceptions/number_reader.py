import json

filename = 'text_files/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)