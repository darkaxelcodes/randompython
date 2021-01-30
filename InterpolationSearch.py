'''
Program to implement Interpolation Search.
The time complexity of above algorithm is O (log log n).
It works on a sorted array.
'''
def interpolation_search(sorted_list_of_digits, digit_to_find):
    length = len(sorted_list_of_digits)
    lo = 0
    hi = length-1
    while sorted_list_of_digits[lo] <= digit_to_find <= sorted_list_of_digits[hi]:
        if lo == hi:
            if digit_to_find == sorted_list_of_digits[lo]:
                return True
            else:
                return False
        elif lo < hi:
            pos = lo + (((digit_to_find-sorted_list_of_digits[lo]) * (hi-lo)) // (sorted_list_of_digits[hi]-sorted_list_of_digits[lo]))
            if digit_to_find == sorted_list_of_digits[pos]:
                return True
            elif digit_to_find < sorted_list_of_digits[pos]:
                return interpolation_search(sorted_list_of_digits[:pos], digit_to_find)
            else:
                return interpolation_search(sorted_list_of_digits[pos+1:], digit_to_find)
    else:
        return False


sorted_list_of_digits = [1,2,3,4,5,6,7,8,9,10]
digit_to_find = int(input("Enter the digit to search: "))
position = interpolation_search(sorted_list_of_digits,digit_to_find)
print("Status of search: {}".format(position))
