# Uses python3
import sys

def get_fibonacci_huge(n, m):
    rem = n%index(m)
    return calc_fib(rem)%m

def calc_fib(n):
    a = 0 
    b = 1
    if n<1:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n):
            arb = b
            b = b+a
            a = arb
        return a+b

def index(m):
    for i in range(2,m*m):
        a = calc_fib(i)%m
        b = calc_fib(i+1)%m
        if (a==0) & (b==1):
            break
    return i

token = input()
token = token.split()
a = token[0]
b = token[1]
print(get_fibonacci_huge(int(a), int(b)))

