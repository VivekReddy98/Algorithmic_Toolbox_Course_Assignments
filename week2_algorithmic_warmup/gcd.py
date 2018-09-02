# Uses python3
import sys

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
print(gcd_naive(int(a), int(b)))