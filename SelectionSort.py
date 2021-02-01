'''
Program to implement Selection Sort
The time complexity of above algorithm is O(n^2)
'''

def selection_sort(list_of_digits):
    for i in range(len(list_of_digits)):
        min = i
        for j in range(i+1, len(list_of_digits)):
            if list_of_digits[j] < list_of_digits[min]:
                min = j
                list_of_digits[i], list_of_digits[min] = list_of_digits[min], list_of_digits[i]
    return list_of_digits

list_of_digits = [10,9,8,7,6,5,4,3,2,1]
sorted_list_of_digits = selection_sort(list_of_digits)
print(sorted_list_of_digits)
