# Сортировка пузырьком

my_list = [1, 9, 7, 8, 2, 3, 0, 4, 6, 5]
print(my_list)

for i in range(len(my_list) - 1, 0, -1):
    no_swap = True
    for j in range(0, i):
        if my_list[j + 1] < my_list[j]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            no_swap = False
    if no_swap:
        my_list

print(my_list)
