'''
Program to implement Jump Search.
The time complexity of above algorithm is O(sqrt(n)).
It works on a sorted array
'''
def linear_search(list_of_numbers,digit_to_find):
    while list_of_numbers is not None:
        for i in range(len(list_of_numbers)):
            if digit_to_find == list_of_numbers[i]:
                return i+1
                break
        else:
            return None

def jump_search(sorted_list_of_digits, digit_to_find, jump_size):
    length = len(sorted_list_of_digits)
    for i in range(0,length,jump_size):
        if digit_to_find <= sorted_list_of_digits[i]:
            if digit_to_find == sorted_list_of_digits[i]:
                return True
                break
            else:
                return linear_search(sorted_list_of_digits[i-jump_size:i],digit_to_find)

sorted_list_of_digits = [1,2,3,4,5,6,7,8,9,10]
digit_to_find = int(input("Enter the digit to search: "))
jump_size = int(input("Enter the jump size: "))
position = jump_search(sorted_list_of_digits,digit_to_find, jump_size)
if position is not None:
    print("Element found")
else: 
    print("Element not found")
