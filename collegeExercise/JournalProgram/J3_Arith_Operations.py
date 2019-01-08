'''
3. Write a program showing  arithmatic operators
'''
a = int(input("Enter Value For A : "))
b = int(input("ENter Value For B : "))

#Addition
c = a + b
print("Addition : ",c)

#Subtraction
c = a - b
print("Subtraction : ",c)

#Multiplication
c = a * b
print("Multiplication : ",c)

#Division
if(b == 0):
    print("Cannot Divide By Zero")
else:
    c = a / b
    print("Division : ",c)


