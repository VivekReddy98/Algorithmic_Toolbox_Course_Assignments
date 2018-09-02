# Uses python3
import sys

def lcm_naive(a, b):
    gcd = gcd_naive(a,b)
    return int((a*b)//gcd)

def gcd_naive(a, b):
    if b>a:
    	temp = b
    	b = a
    	a = temp
    while(b!=0):
    	temp = b
    	b = a%b
    	a = temp
    return a

token = input()
token = token.split()
a = token[0]
b = token[1]
print(lcm_naive(int(a), int(b)))

