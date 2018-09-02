# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2,n):
        arb = b
        b = (b+a)%10
        a = (arb)%10
    return (a+b)%10

n = int(input())
print(get_fibonacci_last_digit_naive(n))
