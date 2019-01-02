'''
    Reading and Writing Csv file
'''
import csv

with open('employee.csv',mode='w') as csv_file:
    fieldname = ['emp_name','dept']
    writer = csv.DictWriter(csv_file,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({'emp_name':'Rushik','dept':'Computer'})

    csv_file.close()

with open('employee.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file,fieldnames=['emp_name','dept'])
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Columns Name Are : {",".join(row)}')
        else:
            print(f'\t {row["emp_name"]} works in {row["dept"]}')

        line_count = line_count + 1
    print(f'Proccessed {line_count} line')