# Пирамидальная сортировка

my_list = [1, 9, 7, 8, 2, 3, 0, 4, 6, 5]
print(my_list)


def heap_sort(my_list):
    build_max_heap(my_list)
    for i in range(len(my_list) - 1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        max_heapify(my_list, index=0, size=i)
    return my_list


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(my_list):
    length = len(my_list)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(my_list, index=start, size=length)
        start = start - 1


def max_heapify(my_list, index, size):
    l = left(index)
    r = right(index)
    if (l < size and my_list[l] > my_list[index]):
        largest = l
    else:
        largest = index
    if (r < size and my_list[r] > my_list[largest]):
        largest = r
    if (largest != index):
        my_list[largest], my_list[index] = my_list[index], my_list[largest]
        max_heapify(my_list, largest, size)


print(heap_sort(my_list))
