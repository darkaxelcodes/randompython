'''
Program to implement Exponential Search.
The time complexity of above algorithm is O(log n).
It works on a sorted array.
'''

def binary_search(sorted_list_of_digits, digit_to_find):
    length = len(sorted_list_of_digits)
    if length == 1:
        if digit_to_find == sorted_list_of_digits[length-1]:
            return True
        else:
            return False
    elif length > 1:
        mid = length//2
        if digit_to_find == sorted_list_of_digits[mid]:
            return True
        elif digit_to_find < sorted_list_of_digits[mid]:
            return binary_search(sorted_list_of_digits[:mid], digit_to_find)
        else:
            return binary_search(sorted_list_of_digits[mid+1:], digit_to_find)

def exponential_search(sorted_list_of_digits,digit_to_find):
    i = 2
    if digit_to_find == sorted_list_of_digits[0]:
        return True
    else:
        found = binary_search(sorted_list_of_digits[:i],digit_to_find)
        if found == True:
            return found
        else:
            i*=2
            found = 


sorted_list_of_digits = [1,2,3,4,5,6,7,8,9,10]
digit_to_find = int(input("Enter the digit to search: "))
position = binary_search(sorted_list_of_digits,digit_to_find)
print("Status of search: {}".format(position))
