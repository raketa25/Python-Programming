import os

file = open('test3.txt', 'w')

file.write('hello from the PATH example')

file.close()

print(os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)))

directory = os.path.dirname(os.path.realpath(__file__))
print(directory)

file_path = os.path.join(directory,'test4.txt')
print(file_path)

'''
file = open(file_path,'w')
file.write('hello from NEW FILE PATH')
file.close()

'''
