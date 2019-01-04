'''
    6.Write a program showing Linear search.
'''
def linear_search(val,search_for):
    search_at = 0
    search_res = False

    while search_at < len(val) and search_res is False:
        if val[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res

l = [64,84,2,10,13]
print(linear_search(l,12))