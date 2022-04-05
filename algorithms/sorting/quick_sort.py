# Быстрая сортировка

my_list = [1, 9, 7, 8, 2, 3, 0, 4, 6, 5]
print(my_list)


def quick_sort(my_list, start, end):
    if end - start > 1:
        p = partition(my_list, start, end)
        quick_sort(my_list, start, p)
        quick_sort(my_list, p + 1, end)
    return my_list


def partition(my_list, start, end):
    pivot = my_list[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and my_list[i] <= pivot):
            i = i + 1
        while (i <= j and my_list[j] >= pivot):
            j = j - 1

        if i <= j:
            my_list[i], my_list[j] = my_list[j], my_list[i]
        else:
            my_list[start], my_list[j] = my_list[j], my_list[start]
            return j


print(quick_sort(my_list, 0, len(my_list)))
