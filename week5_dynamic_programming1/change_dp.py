# Uses python3
import sys

def get_change(m):
    list_new = [0]+[1000]*m
    for j in range(1,m+1):
        result = []
        for i in [1,3,4]:
            dummy = list_new[j]
            if j%i==0:
               dummy = int(j/i)
            elif j%i!=0 and j>=i:
                dummy = list_new[j-i]+1
            result.append(dummy)
        list_new[j] = min(list_new[j],result[0],result[1],result[2])
    return list_new[-1]

token = input()
print(get_change(int(token)))
