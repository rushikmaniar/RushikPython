'''
    Selection sort
'''
list = [5,4,20,1,0]
def selection_sort(list):
    for i in range(len(list)-1):
        for j in range(i,len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

selection_sort(list)
print(list)
