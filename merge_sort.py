import random


def merge(h1, h2):
    """Merge two sorted lists into one and return this list."""
    i = 0
    j = 0
    while i < len(h2):
        num = h2[i]
        while j < len(h1):
            if num < h1[j]:
                h1.insert(j, num)
                break
            elif j == len(h1) - 1:
                h1.append(num)
                break
            j += 1
        i += 1
    return h1


def msort(list_):
    if len(list_) > 1:
        l = 0
        m = len(list_) - (len(list_) // 2)
        r = len(list_)
        return merge(msort(list_[l:m]), msort(list_[m:r]))
    else:
        return list_


list_ = [random.randint(1, 50) for i in range(100)]
sorted_list = msort(list_)
print(sorted_list)

list_.sort()
print("Correct?", sorted_list == list_)
