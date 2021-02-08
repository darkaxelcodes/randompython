'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from 
the list add up to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?

Name : Satyam Srivastava
Date : 18 July 2020
'''
def checkSum(list_of_numbers,k):
    seen = set()
    for number in list_of_numbers:
        if k-number in seen:
            return True
        seen.add(number)
    return False

list_of_numbers = [10,15,3,7,14]
k = 17
result = checkSum(list_of_numbers,k)
print(result)
