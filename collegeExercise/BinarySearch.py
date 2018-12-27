'''
    Binary Searach
'''
print('Binary Search')

def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False

    while (first <= last and not found):
        mid = (first + last) // 2
        if(item_list[mid] == item):
            found = True
        elif item < item_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found

item_list = [10,20.2,35.222,38.002,110.1]
item = 20.2

print(binary_search(item_list,item))