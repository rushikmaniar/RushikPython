'''
    Factorial with Recurssion
'''
temp = 0
print('Recurrsion Example With Factorial ')
def fact(x):
    if(x == 1):
        return 1
    else:
        temp = x * fact(x - 1)
        print(x,' * ',x - 1 , ' = ', temp)
        return temp

num = int(input('Enter no :'))
ans = fact(num)
print('Factorial of ',num,' is ',ans)