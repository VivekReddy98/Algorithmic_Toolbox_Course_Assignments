# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    
    return number_of_inversions

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     b = n * [0]
#     print(get_number_of_inversions(a, b, 0, len(a)))

def merge_sort(a,l,r):
    if len(a)==2:
        if a[l]>a[r]:
            a[l],a[r] = a[r],a[l]
            inversion = inversion+1
        return a[l:r+1]
    elif r==l:
        return a[l:r+1]
    avg = int((r-l)/2)+l
    lower = merge_sort(a,l,avg)
    higher = merge_sort(a,avg+1,r)
    return merge(lower,higher)
        

def merge(lower,higher):
    #print(lower,higher)
    out_array = []
    len_a = len(lower)
    len_b = len(higher)
    while len(out_array)<len_a+len_b:
        if len(lower)==0 and len(higher)!=0:
            out_array.extend(higher)
            del higher
        elif len(higher)==0 and len(lower)!=0:
            out_array.extend(lower)
            del lower
        elif lower[0]>=higher[0]:
            out_array.append(higher[0])
            del higher[0]
        else:
            out_array.append(lower[0])
            del lower[0]
    #print(out_array)
    return out_array

length = input()
token = input()
b = token.split()
b = list(map(int, b))
b_sort = merge_sort(b,0,int(length)-1)
count = 0
for i in range(len(b)):
    value = b[i]-b_sort[i]
    if value==0:
        count = count+1
print(int(length)-count-1)