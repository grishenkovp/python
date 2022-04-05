# Сортировка вставками

my_list = [1, 9, 7, 8, 2, 3, 0, 4, 6, 5]
print(my_list)

for i in range(1, len(my_list)):
    temp = my_list[i]
    j = i - 1
    while (j >= 0 and temp < my_list[j]):
        my_list[j + 1] = my_list[j]
        j = j - 1
    my_list[j + 1] = temp

print(my_list)
