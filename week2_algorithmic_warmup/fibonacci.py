# Uses python3
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
n = int(input())
print(calc_fib(n))
