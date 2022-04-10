# Бинарный поиск
# Бинарный поиск работает по принципу «разделяй и властвуй».
# Он быстрее, чем линейный поиск, но требует, чтобы массив был отсортирован перед выполнением алгоритма.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 7

first = 0
last = len(my_list) - 1
index = -1
while (first <= last) and (index == -1):
    mid = (first + last) // 2
    if my_list[mid] == val:
        index = mid
    else:
        if val < my_list[mid]:
            last = mid - 1
        else:
            first = mid + 1

print(index)