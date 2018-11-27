'''
Amstrong
'''
print("Amstrong Or Not ")
a = int(input("Enter no : "))

temp = a

#find Digits
digit = 0
while temp > 1:
    r = temp % 10
    digit = digit + 1
    temp = temp / 10


temp = a
sum = 0

while temp > 1:
    r = int(temp % 10)
    sum = sum + r ** digit
    temp = temp / 10

if(sum == a):
    print("It Is Amstrong")
else:
    print("Not Amstrong")