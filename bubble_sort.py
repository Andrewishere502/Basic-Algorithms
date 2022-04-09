import random


def bubblesort(list_):
    sorting = True
    while sorting:
        i = 0
        j = 1
        sorting = False
        for _ in range(len(list_) - 1):
            if list_[i] > list_[j]:
                i_val = list_[i]
                j_val = list_[j]
                list_[i] = j_val
                list_[j] = i_val
                sorting = True
            i += 1
            j += 1
            if j == len(list_):
                j = 0
    return


list_ = [random.randint(-10, 10) for _ in range(200)]
print(list_)
bubblesort(list_)
print(list_)
