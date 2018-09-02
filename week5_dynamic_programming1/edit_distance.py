# Uses python3
def edit_distance(a, b):
	a_list = [0] + list(a)
	b_list = [0] + list(b)
	D = []
	for i in range(0,len(a)+1):
		D.append([i])
	for j in range(1,len(b)+1):
		D[0].append(j)
	for j in range(1,len(b)+1):
		for i in range(1,len(a)+1):
			insert = D[i][j-1] + 1
			delete = D[i-1][j] + 1
			if a_list[i] == b_list[j]:
				match = D[i-1][j-1]
			else:
				match = D[i-1][j-1] + 1
			D[i].append(min(insert,delete,match))
	return D[len(a)][len(b)]

str1 = input()
str2 = input()
print(edit_distance(str1, str2))
