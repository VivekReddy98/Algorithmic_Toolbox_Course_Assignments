# Uses python3
import sys

def get_candidate(a,length):
    maj_index = 0
    count = 1
    for i  in range(1,length):
        if a[maj_index]==a[i]:
            count = count+1
        else:
            count = count-1
        if count == 0:
            maj_index = i
            count = 1
    return a[maj_index]

def get_majority_element(a,length):
    cand = get_candidate(a,length)
    count = 0
    for i in range(0,length):
        if a[i]==cand:
            count = count+1
    if count>length/2:
        return 1
    else:
        return 0

length = input()
token = input()
a = token.split()
a = list(map(int, a))
print(get_majority_element(a,int(length)))

