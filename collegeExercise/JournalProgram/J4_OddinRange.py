'''
4. Write a program to list out odd numbers from the given range.
'''
print("Odd in Given Range")
a = int(input("Enter start no : "))
b = int(input("Enter end no : "))


i=a

while i < b:
    if (i % 2 == 1):
        print(i)
    i = i + 1;
