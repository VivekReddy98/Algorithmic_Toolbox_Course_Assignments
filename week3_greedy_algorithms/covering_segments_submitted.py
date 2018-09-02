# Uses python3
import sys

def takeSecond(elem):
    return elem[1]

def optimal_points(num_inputs,s):
    s.sort(key=takeSecond)
    points = []
    #write your code here
    while len(s)!=0:
        ref = s[0][1]
        loneliness = 1
        while len(s)>1 and ref>=s[1][0]:
            if ref>s[1][1]:
                points.append(s[1][1])
            else:
                points.append(ref)
            del s[1]
            loneliness = 0
            if len(s)==1:
                break
        if loneliness == 1:
            points.append(ref)
        del s[0]
    points = list(set(points)) 
    print(len(points))
    print(*points)
    return points
            

token = input()
num_inputs = int(token)
segments = []
for i in range(0,num_inputs):
    token = input()
    token = token.split()
    segments.append((int(token[0]),int(token[1])))
optimal_points(num_inputs,segments)
