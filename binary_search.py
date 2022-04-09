import random


def binary_search(list_, val):
    """Search for a value in a sorted list, return the value if found
    otherwise return None.
    """
    low = 0
    high = len(list_) - 1
    if list_[low] == val:
        return val
    elif list_[high] == val:
        return val

    while True:
        mid = (low + high) // 2
        print(low, high)
        if list_[mid] == val:  # found the value!
            return list_[mid]
        elif low == high - 1:  # val must not be in the list
            return
        elif list_[mid] < val:
            low = mid
        elif list_[mid] > val:
            high = mid


list_ = sorted([random.randint(-10, 10) for _ in range(20)])

print(list(enumerate(list_)))
print(binary_search(list_, 4))
