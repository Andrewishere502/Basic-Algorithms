import random


def partition(list_, low, high):
    pivot = list_[high]
    i = low - 1

    for j in range(low, high):
        if list_[j] <= pivot:
            i += 1
            i_val = list_[i]
            j_val = list_[j]
            list_[i] = j_val
            list_[j] = i_val
    i_val = list_[i + 1]
    high_val = list_[high]
    list_[i + 1] = high_val
    list_[high] = i_val
    return i + 1  # index of the partition's new place


def quicksort(list_, low, high):
    if low < high:
        i = partition(list_, low, high)

        quicksort(list_, low, i - 1)
        quicksort(list_, i + 1, high)
    return



# list_ = [10, 80, 30, 90, 40, 50, 70]
list_ = [random.randint(-100, 100) for _ in range(10)]

print(list_)

quicksort(list_, 0, len(list_) - 1)

print(list_)
