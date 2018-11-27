'''
1 To 10 Or 10 to 1
'''

start = int(input("Enter start no : "))
end = int(input("Enter end no : "))
print("Enter 1 to print ",start," to ",end)
print("Enter 2 to print ",end," to ",start)
choice = int(input("Enter choice : "))
if (choice == 1 or choice == 2):
    temp = start
    while temp <= end:
        if (choice == 1):
            print(temp)
        elif(choice == 2):
            print(end + 1 - temp)
        temp = temp + 1
else:
    print("Invalid choice")
