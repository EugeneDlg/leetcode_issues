from collections import defaultdict
from typing import List


def findMaximumXOR(nums: List[int]) -> int:
    dct = defaultdict(list)
    mask = 1
    max_sum = 0
    for i in range(31, -1, -1):
        for e in nums:
            key = e >> i
            dct[key].append(e)
        for e in dct:
            if dct.get(e ^ mask) is not None:
                max_sum |= 1 << i
                break
        else:
            mask -= 1
        dct.clear()
        mask = mask << 1 | 1
    return max_sum
