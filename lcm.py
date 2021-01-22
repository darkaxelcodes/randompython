# Uses python3
import sys
def eucledianGCD(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a < b:
        return eucledianGCD(a,b%a)
    else:
        return eucledianGCD(a%b,b)

def lcm_efficient(a, b):
    gcd = eucledianGCD(a,b)
    return (a*b)//gcd

a,b = map(int,input().split())
LCM = lcm_efficient(a, b)
print(LCM)
