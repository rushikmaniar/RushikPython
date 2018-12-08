class Employee:
    EmpCount = 0


    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.EmpCount += 1

    def displayCount (self):
        print('No Of Employees : ',Employee.EmpCount)

    def displayEmployee(self):
        print('Name : ',self.name)
        print('Salary : ',self.salary)

emp1 = Employee('Rushik',1500)
emp1.displayCount()

emp1.displayEmployee()
