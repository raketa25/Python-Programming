file = open('test.txt', 'r')
message = file.read()
file.close()

print(message)

with open('test2.txt', 'r') as file2:
  message2 = file2.read()

print(message2)