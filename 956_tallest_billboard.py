import copy
from collections import defaultdict
from time import perf_counter

# rods = [ 1, 2, 2, 4, 10]
rods = [1, 2, 3, 3, 3, 7, 2]
rods = [1, 1, 1, 1, 2, 2, 3]
rods = [1, 1000000000]
# rods = [2, 2]
# s[5] = {3: [1, 2], (3, 1): [{3: 1, 2: 1, 2: 1}, {3: 1, 1: 1}, {3: 1, 2: 2}]}
#
#
#


class Solution:
    def tallestBillboard_0(self, rods: list[int]) -> int:
        def diff_h(rods: list[int]) -> dict[int, int]:
            dh = {0: 0}
            for rod in rods:
                for d, h in list(dh.items()):
                    dh[d + rod] = max(dh.get(d + rod, 0), h)
                    dh[abs(d - rod)] = max(dh.get(abs(d - rod), 0), h + min(d, rod))
            return dh

        d1, d2 = diff_h(rods[: len(rods) // 2]), diff_h(rods[len(rods) // 2 :])
        return max(v1 + d2[k1] + k1 for k1, v1 in d1.items() if k1 in d2)

    def tallestBillboard_1(self, rods: list[int]) -> int:
        rods.sort()
        max_height = 0
        heights = sum(rods) + 1
        dct = [0] * heights
        for i in rods:
            dct[i] += 1
        synthetic = defaultdict(dict)
        for e in rods:
            synthetic[e] = {(e, 1): [defaultdict(int)]}
            synthetic[e][(e, 1)][0][e] = 1

        for i in range(2, heights // 2 + 1):
            next_i = False
            prev = None
            for j in rods:
                if i - j < 1:
                    break
                if j == prev:
                    continue
                prev = j
                if synthetic.get(i - j):
                    new_temp_lst = []
                    flag = False
                    for key in synthetic[i - j]:
                        if key == (j, dct[j]):
                            continue
                        new_local_temp_lst = []
                        if key[0] == j:
                            flag = True
                            for factor_dct in synthetic[i - j][key]:
                                new_dct = factor_dct.copy()
                                new_dct[j] += 1
                                new_local_temp_lst.append(new_dct)
                            synthetic[i][j, key[1] + 1] = copy.deepcopy(new_local_temp_lst)
                        else:
                            for factor_dct in synthetic[i - j][key]:
                                if factor_dct.get(j) and factor_dct[j] == dct[j]:
                                    continue
                                new_dct = factor_dct.copy()
                                new_dct[j] += 1
                                new_temp_lst.append(new_dct)
                                new_local_temp_lst.append(new_dct)
                            if len(new_local_temp_lst) > 0:
                                synthetic[i][key] = copy.deepcopy(new_local_temp_lst)
                    if not flag and len(new_temp_lst) > 0:
                        synthetic[i][(j, 1)] = copy.deepcopy(new_temp_lst)
                        new_temp_lst.clear()
                        flag = False
            values = []
            for value in synthetic[i].values():
                for item in value:
                    values.append(item)
            for index_0, value_0 in enumerate(values):
                if next_i:
                    break
                for index_1 in range(index_0, len(values)):
                    value_1 = values[index_1]
                    # local_height = 0
                    for key in set(value_0.keys()).union(set(value_1.keys())):
                        qty_0 = value_0.get(key) if value_0.get(key) else 0
                        qty_1 = value_1.get(key) if value_1.get(key) else 0
                        if qty_0 + qty_1 > dct[key]:
                            break
                        # else:
                        #     local_height += key * (qty_0 + qty_1)
                    else:
                        max_height = i
                        next_i = True
                        break
            print(i, values)

