import random


# this makes a pythagorean tripple

m = random.randint(1, 5)
n = random.randint(1, m - 1)

a = m ** 2 - n ** 2
b = 2 * m * n
c = m ** 2 + n ** 2

print(a, b, c)
