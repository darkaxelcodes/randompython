'''
Program to implement Selection Sort
The time complexity of above algorithm is O(n^2)
'''
def find_min (list0):
    min = 0
    for i in range(1,len(list0)):
        if list0[i] < list0[min]:
            min = i
    return min

def selection_sort(list0):
    i = 0
    while i < len(list0):
        pos = find_min(list0[i:])
        if pos != 0:
            list0[i], list0[pos+i] = list0[pos+i], list0[i]
        i+=1
    return list0

list0 = [10,9,8,7,6,5,4,3,2,1]
sorted_list0 = selection_sort(list0)
print(sorted_list0)