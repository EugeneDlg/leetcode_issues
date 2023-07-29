from typing import List, Dict
import copy
from collections import defaultdict
from time import perf_counter

# rods = [1, 2, 3, 3, 3, 7, 2, 10, 12, 5, 3, 14]
# rods = [1, 2, 3, 3, 3, 7, 2, 10, 12, 5, 3]
# rods = [1, 2, 3, 3, 3, 3,3,3, 3, 4, 5, 6, 7, 2, 10, 5, 3, 12, 33, 23, 100, 150, 60]
rods = [1, 2, 3, 3, 3, 3,3,3, 3, 4, 5, 6, 7, 2, 10, 5, 3, 11, 2, 70, 100, 50, 30, 20, 100]
# rods = [1, 1, 1, 1, 2, 2, 3, 15]
# rods = [1, 1, 2, 3, 2, 1]

# rods = [2, 2]
# s[5] = {3: [1, 2], (3, 1): [{3: 1, 2: 1, 2: 1}, {3: 1, 1: 1}, {3: 1, 2: 2}]}
#
#
#


class Solution:
    def tallestBillboard_0(self, rods: List[int]) -> int:
        def diff_h(rods: List[int]) -> Dict[int, int]:
            dh = {0: 0}
            for rod in rods:
                for d, h in list(dh.items()):
                    dh[d + rod] = max(dh.get(d + rod, 0), h)
                    dh[abs(d - rod)] = max(dh.get(abs(d - rod), 0), h + min(d, rod))
            return dh

        d1, d2 = diff_h(rods[: len(rods) // 2]), diff_h(rods[len(rods) // 2:])
        return max(v1 + d2[k1] + k1 for k1, v1 in d1.items() if k1 in d2)

    def tallestBillboard_1(self, rods: List[int]) -> int:
        memo_dct = {}

        def memoize(dct: dict):
            h = hash(frozenset(dct.items()))
            memo_dct[h] = dct
            return h
        rods.sort()
        heights = sum(rods) + 1
        dct = [0] * heights
        for i in rods:
            dct[i] += 1
        partition = defaultdict(dict)
        for e in rods:
            d = defaultdict(int)
            d[e] = 1
            partition[e] = {(e, 1): {memoize(d)}}
        for i in range(2, heights // 2 + 1):
            prev = None
            for j in rods:
                if i - j < 1:
                    break
                if j == prev:
                    continue
                prev = j
                if partition.get(i - j):
                    new_temp_lst = set()
                    flag = False
                    for key in partition[i - j]:
                        if key == (j, dct[j]):
                            continue
                        new_local_temp_lst = set()
                        if key[0] == j:
                            flag = True
                            for hash_ in partition[i - j][key]:
                                new_dct = memo_dct[hash_].copy()
                                new_dct[j] += 1
                                new_local_temp_lst.add(memoize(new_dct))
                            partition[i][j, key[1] + 1] = new_local_temp_lst
                        else:
                            for hash_ in partition[i - j][key]:
                                factor_dct = memo_dct[hash_]
                                if factor_dct.get(j) and factor_dct[j] == dct[j]:
                                    continue
                                new_dct = factor_dct.copy()
                                new_dct[j] += 1
                                m = memoize(new_dct)
                                new_temp_lst.add(m)
                                new_local_temp_lst.add(m)
                            if len(new_local_temp_lst) > 0:
                                if not partition[i].get(key):
                                    partition[i][key] = new_local_temp_lst
                                else:
                                    partition[i][key].union(new_local_temp_lst)
                    if not flag and len(new_temp_lst) > 0:
                        partition[i][(j, 1)] = new_temp_lst
                        flag = False
        for i in range(heights // 2, 1, -1):
            values_set = set()
            for value in partition[i].values():
                for hash_ in value:
                    values_set.add(hash_)
            while len(values_set):
                hash_0 = values_set.pop()
                for hash_1 in {hash_0}.union(values_set):
                    value_0 = memo_dct[hash_0]
                    value_1 = memo_dct[hash_1]
                    for key in set(value_0.keys()).union(set(value_1.keys())):
                        qty_0 = value_0.get(key) if value_0.get(key) else 0
                        qty_1 = value_1.get(key) if value_1.get(key) else 0
                        if qty_0 + qty_1 > dct[key]:
                            break
                    else:
                        return i
        return 0


t0 = perf_counter()
solution_0 = Solution().tallestBillboard_0(rods)
t1 = perf_counter()
solution_1 = Solution().tallestBillboard_1(rods)
t2 = perf_counter()
print(solution_0)
print(solution_1)
print("Time: ", t1-t0)
print("Time: ", t2-t1)