file_path = input("Please provide the file path you want to convert: ")

with open(file_path, 'rU') as input_file:
     processed_contents = input_file.read()
     # conversion function

processed_file_path = input("Please provide the new file name for the processed file: ")

with open(processed_file_path, 'w') as processed_file:

    processed_file.write(processed_contents) 

print("Here is the converted result: ")
print(processed_contents)  