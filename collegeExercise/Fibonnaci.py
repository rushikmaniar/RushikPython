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
'''
if n <= 0:
    print('Enter Positive Number : ')
else:
    for i in range(n):
        print(recur_fibo(i))'''


print("\n\n Using While loop")
prev=0
current=1
next_current = 1
i = 0
print("0\n1")
while(i < n-2):
    prev = current
    current = next_current
    print(current)
    next_current = prev + current
    i = i + 1








