from collections import defaultdict
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins_ = []
        combinations = defaultdict(int)
        for e0 in coins:
            coins_.append(e0)
            for e1 in range(amount+1):
                if e1 == 0:
                    combinations[e1] = 1
                # elif e1 < coins_[-1]:
                #     combinations[e1] = combinations[e1, tuple(coins_[:-1]))]
                elif e1 >= coins_[-1]:
                    combinations[e1] = combinations[e1] + combinations[e1 - coins_[-1]]

        return combinations[amount]