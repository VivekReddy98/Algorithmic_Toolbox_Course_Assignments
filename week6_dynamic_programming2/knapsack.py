# Uses python3
import sys

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
	return D[num_bars][W]
    # # write your code here
    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result

token = input()
Weight,num_bars = token.split()
Weights_bars = input()
print(optimal_weight(int(Weight), int(num_bars), list(map(int, Weights_bars.split()))))
