import random
import time


def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("function call '%s' took %s seconds" % (func.__name__, time.time() - start_time))
        return result
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


@timer
def unordered_list():
    return [random.randrange(1,90000) for _ in range(25)]


@timer
def ordered_list():
    return [n for n in range(25)]


# ----------------- algorithms -----------------


def get_index(list_, low, val):
    """Basically sequencial sort, but cropped to be a little
    more efficient.
    """
    for i, item in enumerate(list_[low:]):
        if item == val:
            return low + i
    return


def selection_sort(list_):
    """Sort the list itself, not a copy. Returns None.
    Efficiency: O(n^2)
    """
    i = 0
    for _ in list_:
        lowest_i = get_index(list_, i, min(list_[i:]))
        i_val = list_[i]
        lowest_i_val = list_[lowest_i]
        list_[i] = lowest_i_val
        list_[lowest_i] = i_val
        i += 1
    return


def bubble_sort(list_):
    """Sort the list itself, not a copy. Returns None.
    Efficiency: O(n^2)
    """
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
 

def sequential_search(list_, target):
    """Return the index of the target in a list.
    Efficiency: O(n)
    """
    for i, item in enumerate(list_):
        if item == target:
            return i
    return


def binary_search(list_, target):
    """Search for a value in a sorted list, return the index of the
    value if found otherwise return None.
    Efficiency: O(n/2)
    """
    low = 0
    high = len(list_) - 1
    if list_[low] == target:
        return low
    elif list_[high] == target:
        return high

    while True:
        mid = (low + high) // 2
        if list_[mid] == target:  # found the value!
            return mid
        elif low == high - 1:  # val must not be in the list
            return
        elif list_[mid] < target:
            low = mid
        elif list_[mid] > target:
            high = mid
    return


if __name__ == "__main__":
    numberToFind = 700

    # user the timer wrapper to time a function

    print(ordered_list())