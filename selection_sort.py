import random


def get_index(list_, low, val):
    for i, item in enumerate(list_[low:]):
        if item == val:
            return low + i
    return


def selection_sort(list_):
    i = 0
    for _ in list_:
        lowest_i = get_index(list_, i, min(list_[i:]))
        i_val = list_[i]
        lowest_i_val = list_[lowest_i]
        list_[i] = lowest_i_val
        list_[lowest_i] = i_val
        i += 1
    return


list_ = [random.randint(-10, 10) for _ in range(50)]

print(list_)
selection_sort(list_)
print(list_)
