'''
Program to implement Bubble Sort
The time complexity of above algorithm is 
'''

def bubble_sort(list_of_digits):
    swap_count = 0
    for i in range(len(list_of_digits)-1):
        if list_of_digits[i] > list_of_digits[i+1]:
            list_of_digits[i], list_of_digits[i+1] = list_of_digits[i+1], list_of_digits[i]
            swap_count+=1
    if swap_count != 0:
        return bubble_sort(list_of_digits)
    return list_of_digits
           


list_of_digits = [10,9,8,7,6,5,4,3,2,1]
sorted_list_of_digits = bubble_sort(list_of_digits)
print(sorted_list_of_digits)
