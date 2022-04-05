# Сортировка слиянием

my_list = [1, 9, 7, 8, 2, 3, 0, 4, 6, 5]
print(my_list)


def merge_sort(my_list, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(my_list, start, mid)
        merge_sort(my_list, mid, end)
        merge_list(my_list, start, mid, end)
    return my_list


def merge_list(my_list, start, mid, end):
    left = my_list[start:mid]
    right = my_list[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            my_list[k] = left[i]
            i = i + 1
        else:
            my_list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            my_list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            my_list[k] = right[j]
            j = j + 1
            k = k + 1


print(merge_sort(my_list, 0, len(my_list)))
