# Uses python3
import sys
import itertools

def partition3(A):
    W = int(sum(A)/3)
    #print(W)
    if sum(A)%3!=0:
        return 0
    else:
        D = optimal_weight(W, len(A), A)
        #print(D)
        if D[-1][-1]!=W:
            return 0
        else:
            #print(D)
            return backtrack(D,A,W)


def backtrack(D,A,W):
    num_partitions = 0
    for i in reversed(range(len(A)+1)):
        if D[i][W] == D[i-1][W]:
            if D[i-1][W] == D[i-1][W-A[i-1]]+A[i-1]:
                num_partitions = num_partitions+1
    #print(num_partitions)
    if num_partitions>=2:
        return 1
    else:
        return 0

def optimal_weight(W, num_bars, weight_bars):
    D = []
    for i in range(0,num_bars+1):
        D.append([0])
    for j in range(1,W+1):
        D[0].append(0)
    for i in range(1,num_bars+1):
        for j in range(1,W+1):
            if j<weight_bars[i-1]:
                D[i].append(D[i-1][j])
            else:
                opt = max(D[i-1][j],D[i-1][j-weight_bars[i-1]]+weight_bars[i-1])
                D[i].append(opt)
    return D


waste = input()
A = input()
A = list(map(int, A.split()))
print(partition3(A))
#print([1,2,3,4,5,5,7,7,8,10,12,19,25])
#print(partition3(A))

