# Uses python3
import sys

def get_change(m):    #write your code here
    tens = int(m/10)
    fives = int((m-10*tens)/5)
    ones = m - 10*tens - 5*fives
    return tens+fives+ones
    
token = input()
print(get_change(int(token)))
