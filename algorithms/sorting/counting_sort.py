# Сортировка подсчетом

my_list = [1, 9, 7, 8, 2, 3, 0, 4, 6, 5]
print(my_list)


def counting_sort(my_list, largest):
    c = [0] * (largest + 1)
    for i in range(len(my_list)):
        c[my_list[i]] = c[my_list[i]] + 1

    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(my_list)

    for x in reversed(my_list):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result

print(counting_sort(my_list, max(my_list)))