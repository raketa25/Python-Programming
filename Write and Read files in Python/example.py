with open('data.txt', 'r') as file:
    record = file.read()

print(record)

record = record.split('\n')

# print(record)

with open('report.html', 'w') as report:
    report.write('<table>')
    for student in record:
        if 'boy' in student:
            value = student.split(',')
            result = '<tr>'
            for item in value:
                result += f'<td>{item}</td>'
            report.write(f'{result}</tr>')
    report.write('</table>')