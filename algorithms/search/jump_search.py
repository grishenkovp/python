# Jump Search
import math

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 5


def jump_search(my_list, val):
    length = len(my_list)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and my_list[left] <= val:
        right = min(length - 1, left + jump)
        if my_list[left] <= val and my_list[right] >= val:
            break
        left += jump;
    if left >= length or my_list[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and my_list[i] <= val:
        if my_list[i] == val:
            return i
        i += 1
    return -1


print(jump_search(my_list, val))
