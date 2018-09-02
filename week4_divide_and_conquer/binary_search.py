# Uses python3
import sys

def final(num_inputs,Queries):
    left, right = 0,len(num_inputs)-1
    list_out = []
    for i in Queries:
        left, right = 0, len(num_inputs)
        list_out.append(binary_search(num_inputs, i, left, right))
    return list_out


def binary_search(num_inputs, value, left, right):
    if num_inputs[right-1]<value or num_inputs[left]>value:
       return -1
    while left <= right :
        mid = int((right-left)/2)+left
        if num_inputs[mid] == value :
            return mid
        if value < num_inputs[mid]:
            right = mid-1
        else:
            left  = mid+1
    return -1
 


token = input()
num_inputs = token.split()[1:]
num_inputs = list(map(int, num_inputs))
token = input()
Queries = token.split()[1:]
Queries = list(map(int, Queries))
print('\t'.join(map(str, final(num_inputs, Queries))))




