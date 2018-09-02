# Uses python3
import sys

def get_optimal_value(capacity, weights, values, unit_cost):
    value = 0.0000
    while (capacity>0 and len(weights)>0):
    	index_max = unit_cost.index(max(unit_cost))
    	if capacity>=weights[index_max]:
    		value = value+values[index_max]
    	else:
    		value = value+(values[index_max]*capacity/weights[index_max])
    	capacity = capacity-weights[index_max]
    	del unit_cost[index_max],weights[index_max],values[index_max]          
    return round(value,4)


token = input()
token = token.split()
num_inputs = int(token[0])
capacity = int(token[1])
values = []
weights = []
unit_cost = []
for i in range(0,num_inputs):
	token = input()
	token = token.split()
	values.append(int(token[0]))
	weights.append(int(token[1]))
	unit_cost.append(int(token[0])/int(token[1]))
print(get_optimal_value(capacity, weights, values, unit_cost))
