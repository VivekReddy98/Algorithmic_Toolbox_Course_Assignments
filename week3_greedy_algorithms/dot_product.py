#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a.sort(reverse=True)
    b.sort(reverse=True)
    return sum([c*d for c,d in zip(a,b)])

if __name__ == '__main__':
    num_inputs = input()
    ads = input()
    ads = list(map(int,ads.split()))
    slots = input()    
    slots = list(map(int,slots.split()))
    print(max_dot_product(ads, slots))
