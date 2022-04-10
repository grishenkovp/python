# Сортировка Шелла
import math

my_list = [1, 9, 7, 8, 2, 3, 0, 4, 6, 5]
print(my_list)

n = len(my_list)
k = int(math.log2(n))
interval = 2 ** k - 1
while interval > 0:
    for i in range(interval, n):
        temp = my_list[i]
        j = i
        while j >= interval and my_list[j - interval] > temp:
            my_list[j] = my_list[j - interval]
            j -= interval
        my_list[j] = temp
    k -= 1
    interval = 2 ** k - 1

print(my_list)