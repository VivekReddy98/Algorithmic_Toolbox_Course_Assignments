# Uses python3
import sys

def optimal_sequence_operations(n):
    result = []
    result.append(1)
    result.append(0) 
    i = 2
    for i in range(2,n+1):
        min1 = result[i-1] + 1
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i%2==0:
            min2 = result[int(i/2)]+1
        if i%3==0:
            min3 = result[int(i/3)]+1
        result.append(min(min1,min2,min3))
    return result

def steps_taken(n):
    result = optimal_sequence_operations(n)
    ops = result[-1]
    sequence = []
    sequence.append(n)
    for i in range(0,ops):
        ops1 = result[n-1]
        ops2 = sys.maxsize
        ops3 = sys.maxsize
        if n%2==0:
            ops2 = result[int(i/2)]
        if n%3==0:
            ops3 = result[int(i/3)]
        opsmin = min(ops1,ops2,ops3)
        if ops1 == opsmin:
            n = n-1
        elif ops2 == min(ops1,ops2,ops3):
            n = int(n/2)
        else:
            n = int(n/3)

        sequence.append(n)
    print(ops)
    sequence[-1] = 1
    sequence.reverse()
    return sequence



n = input()
print(' '.join(map(str, steps_taken(int(n)))))
