def eucledianGCD(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a < b:
        return eucledianGCD(a,b%a)
    else:
        return eucledianGCD(a%b,b)

a,b = map(int,input().split())
GCD = eucledianGCD(a,b)
print(GCD)
