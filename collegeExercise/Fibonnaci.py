'''
    Fibonacci series
'''

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


print('Fibonacci Series')
n = int(input('Enter Length Of Series:'))

if n <= 0:
    print('Enter Positive Number : ')
else:
    for i in range(n):
        print(recur_fibo(i))




