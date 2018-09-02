# Uses python3
import sys
import random

def partition3(a, l, r):
    m1 = l
    m2 = l+1
    for i in range(l+1,r+1):
        if a[i]<a[m1]:
            a[m2],a[i] = a[i],a[m2]
            a[m2],a[m1] = a[m1],a[m2]
            m1 = m1+1
            m2 = m2+1
        elif a[i]==a[m1]:
            a[i],a[m2] = a[m2],a[i]
            m2 = m2+1
    return m1,m2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return 
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1,m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2, r);
    return a


length = input()
token = input()
a = token.split()
a = list(map(int, a))
print('\t'.join(map(str, randomized_quick_sort(a, 0, len(a)-1))))

