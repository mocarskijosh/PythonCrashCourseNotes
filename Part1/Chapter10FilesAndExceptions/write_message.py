filename = 'text_files/programming.txt'

# Can open files in - r (read), w (write), a (append)
# open function with create the file if it doesn't already exist
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")