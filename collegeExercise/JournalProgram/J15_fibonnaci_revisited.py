'''
    15.Write a program to print Fibonnaci Serises (Fastfib)
'''
def fastfib(n,memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastfib(n-1,memo) + fastfib(n-2,memo)
        memo[n] = result
        return result

n=10
print('Series')
for i in range(n):
    print(fastfib(i))