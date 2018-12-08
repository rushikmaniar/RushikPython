try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = a / b
    raise ZeroDivisionError
except Exception as e:
    print('Custom : ',e)