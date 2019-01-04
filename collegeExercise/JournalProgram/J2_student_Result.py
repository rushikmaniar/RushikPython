'''
2. Write a program to find out the result of a student.(Use elif statement)
'''
print('Student Result Program')
m1=int(input('Enter Mark1:'))
m2=int(input('Enter Mark2:'))
m3=int(input('Enter Mark3:'))
total=m1+m2+m3
per=total/3
if(m1 < 35 or m2 < 35 or m3 < 35):
    print('Student is fail')
else:
    if(per < 50):
        print('Total:',total,' Percentage :' ,per,' Grade : C')
    elif(per < 70):
        print('Total:', total, ' Percentage :', per, ' Grade : B')
    elif(per < 90):
        print('Total:', total, ' Percentage :', per, ' Grade : A')
    else:
        print('Total:', total, ' Percentage :', per, ' Grade : A+')