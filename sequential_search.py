import random


def seq_search(list_, val):
    for i, item in enumerate(list_):
        if item == val:
            return i
    return


list_ = [random.randint(-10, 10) for _ in range(50)]

print(list_)
print(seq_search(list_, 4))
