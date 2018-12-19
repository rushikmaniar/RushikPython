'''
    Bubbble sort
'''
def bubble_sort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp

list = [19,2,31,45,7]
bubble_sort(list)
print(list)