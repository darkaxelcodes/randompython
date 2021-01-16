def calculate_fib(n):
    array = [0,1,1]
    for i in range(3,n+1):
        length = len(array)
        next = array[length-1] + array[length-2]
        array.append(next)
    if n == 0:
        return 0
    elif n == 1:
        return [0,1]
    else:
        return array
    
n = int(input("Enter the number of terms you want in the fibbonacci sequence: "))
#result = calculateFib(n)
print(calculate_fib(n))
