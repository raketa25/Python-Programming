"""
- This 
"""
file_name = 'file.txt'

try:
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)
except NameError as name_error:
    print(f'There was a NameError: {name_error}')
except FileNotFoundError as file_error:
    print(f'There was a FileNotFoundError: {file_error}')
else:
    print(data)
finally:
    print('The script is finished.')