'''
    shell Sort
'''
def shellsort(input_list):
    gap = len (input_list)

    while gap > 0:
        for i in range (gap,len(input_list)):
            temp = input_list[i]
            j = i

            while j >= gap and input_list[j-gap] > temp:
                input_list[j] = input_list[j-gap]
                j = j - gap
                input_list[j] = temp
        gap = gap // 2
list = [19,2,31,30,11,121]
shellsort(list)
print(list)