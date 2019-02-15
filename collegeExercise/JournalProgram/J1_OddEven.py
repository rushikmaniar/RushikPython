'''
1. Write a python program to find out a number is odd or even.
'''
print("Odd Or Even")
a = int(input("Enter no : "))

if (a == 0):
    print('A is Zero')
elif(a % 2 == 0):
    print('A is Even')
else:
    print('A is Odd')
