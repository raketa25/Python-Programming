# Basic lists
test_list = ['bob', 'sue', 'fred', 'pat', 99]

print(test_list)

print(test_list[1])

for x in test_list:
  print(x)

# Sorting a list in python
test_list = ['bob', 'sue', 'fred', 'pat']

test_list.sort()
#test_list.sort(reverse=True)

print(test_list)

# Add and remove elements from a list in python
test_list = ['bob', 'sue', 'fred', 'pat']

print(test_list)

test_list.append('tommy')

print(test_list)

test_list.insert(1, 'sally')

print(test_list)

test_list.remove('bob')

print(test_list)

test_list.pop(1)

print(test_list)

# Splitting a list
record = 'bob, tim, tom, tammy, phil'

print(record)

record = record.split(',')

print(record)

for x in record:
  x = x.strip()
  print(x)

# Dictionaries
test_dict = {'name':'fred', 'age':22, 'shirt_size':'large'}

print(test_dict)

print(test_dict['age'])

# for x in test_dict:
#   #print(x)

# Another way
for x in test_dict:
  print(test_dict[x])

for x, y in test_dict.items():
  print(x, y)


# Add and remove elements from a dictionary in python
test_dict = {'name':'fred', 'age':22, 'shirt_size':'large'}

print(test_dict)

test_dict['shirt_size'] = 'small'

print(test_dict)

test_dict['allergy'] = 'peanut'

print(test_dict)

test_dict.pop('age')

print(test_dict)

# Nested list
class_list = [{'name':'fred', 'age':20, 'shirt_size':'large'},
              {'name':'sue', 'age':18, 'shirt_size':'small'},
              {'name':'pat', 'age':30, 'shirt_size':'medium'},
              {'name':'tim', 'age':25, 'shirt_size':'small'}]

for record in class_list:
  print(record)

for record in class_list:
  print(f"{record['name']} {record['age']} {record['shirt_size']}")

for record in class_list:
  if record['shirt_size'] == 'small':
    print(f"{record['name']} {record['age']} {record['shirt_size']}")