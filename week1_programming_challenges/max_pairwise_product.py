# python3


def max_pairwise_product(numbers):
    max_number = 0
    second_max = 0
    for i in range(len(input_numbers)):
        if input_numbers[i] >= max_number:
            max_number = input_numbers[i]
            index = i
    #print(index)
    for j in range(len(input_numbers)):
        if (input_numbers[j] >= second_max)  &  (j != index):
            second_max =  input_numbers[j]
            #print(j)   
    return max_number*second_max


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
