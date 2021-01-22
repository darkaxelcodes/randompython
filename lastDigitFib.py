def calculateFib(n):
    array = [0,1,1]
    for i in range(3,n+1):
        length = len(array)
        next = array[length-1] + array[length-2]
        array.append(next%10)
    length = len(array)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return array[-1]
    
n = int(input())
#result = calculateFib(n)
print(calculateFib(n))
