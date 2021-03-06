'''
    Merge Sort
'''
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    leftlist = unsorted_list[:middle]
    rightlist = unsorted_list[middle:]

    leftlist = merge_sort(leftlist)
    rightlist = merge_sort(rightlist)
    return list(merge(leftlist,rightlist))


def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])

    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


list1 = [5,2,15,8,65]
list1 = merge_sort(list1)
print(list1)