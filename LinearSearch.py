'''
Program to implement Linear Search.
The time complexity of above algorithm is O(n).
'''

def linear_search(list_of_numbers,digit_to_find):
    while list_of_numbers is not None:
        for i in range(len(list_of_numbers)):
            if digit_to_find == list_of_numbers[i]:
                return i+1
                break
        else:
            return None

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
digit_to_find = int(input("Enter the digit to search: "))
position = linear_search(list_of_numbers,digit_to_find)
print("The digit is found at position: {}".format(position))
