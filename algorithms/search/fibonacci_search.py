# Fibonacci Search

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 5


def fibonacci_search(my_list, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(my_list)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(my_list) - 1))
        if (my_list[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (my_list[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if (fibM_minus_1 and index < (len(my_list) - 1) and my_list[index + 1] == val):
        return index + 1;
    return -1


print(fibonacci_search(my_list, val))
