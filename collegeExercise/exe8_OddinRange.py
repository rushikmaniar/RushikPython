'''
Odd in Given Range
'''
print("Odd in Given Range")
a = int(input("Enter start no : "))
b = int(input("Enter end no : "))


i=a

while i < b:
    if (i % 2 == 1):
        print(i)
    i = i + 1;
