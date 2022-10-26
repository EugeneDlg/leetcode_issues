from math import sqrt, floor
import time
import re


def func(c):
    if c == 0: return True
    sq = sqrt(c)
    if sq == floor(sq): return True
    sq = sqrt(c / 2)
    if sq == floor(sq): return True
    sq = sqrt(c - 1)
    if sq == floor(sq): return True
    if c % 4 == 3: return False
    for i in range(2, int(sqrt(c)) + 1):
        ii = 0
        while (c % i == 0):
            c = c / i
            ii += 1
        if i % 4 == 3 and ii % 2 != 0: return False
    if c % 4 == 3: return False
    return True


def func_bf(c):
    """
    return True if d0 == 0 or sqrt(d0) == int(sqrt(d0)) or sqrt(d0/2) == int(sqrt(d0/2)) or sqrt(d0-1) == int(sqrt(d0-1)) else return False
"""
    if c == 0: return True
    sq = sqrt(c)
    if sq == floor(sq): return True
    sq = sqrt(c / 2)
    if sq == floor(sq): return True
    sq = sqrt(c - 1)
    if sq == int(sq): return True
    for i in range(2, floor(sqrt(c / 2)) + 1):
        s0 = sqrt(c - i ** 2)
        if s0 == int(s0): break
    else:
        return False
    return True

# d0 = int(input('Enter a non-negative integer: '))
# #print('Yes') if func(d0) else print('No')
# print('Yes') if func(d0) else print('No')
