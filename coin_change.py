from collections import defaultdict
from typing import List
combinations = {}

class Solution:
    def coinChange(self, coins: List[int], amount: int):
        changes = {}
        coins.sort()
        for e in coins:
            changes[e] = 1
            combinations[e] = e
        start_position = coins[0]
        for i in range(start_position, amount+1):
            for e in coins:
                if i <= e:
                    break
                if changes.get(i-e) is not None:
                    if changes.get(i) is None:
                        changes[i] = 1 + changes[i-e]
                        combinations[i] = [e,combinations[i-e]]
                    else:
                        changes[i] = min(changes[i], 1 + changes[i-e])
                        combinations[i].extend([e, combinations[i - e]])
        return changes[amount] if changes.get(amount) is not None else -1


print(Solution().coinChange([2,3], 11))
print(combinations[11])
#
#
#     def coinChange2(self, coins: List[int], amount: int):
#         changes = {}
#         counter = 0
#         counter_down = 0
#         coins.sort()
#         for e in coins:
#             changes[e] = 1
#         start_position = coins[0]
#         for i in range(start_position, amount+1):
#             for e in coins:
#                 if i <= e:
#                     break
#                 if changes.get(i-e) is not None:
#                     counter += 1
#                     if i-e  in coins and i-e != e:
#                         counter_down += 1
#                     if changes.get(i) is None:
#                         changes[i] = 1 + changes[i-e]
#                     else:
#                         changes[i] = min(changes[i], 1 + changes[i-e])
#         print(changes)
#         return counter, counter_down
#
#
# # in_coins = [5, 7, 8, 11, 17, 19, 21, 27, 31]
# in_coins = [2, 3]
# print(Solution().coinChange2(in_coins, 11))


# class recursiveSolution:
#     def coinChange(self, coins: List[int], amount: int):
#         r = Solution.find_coins(coins, amount)
#
#     @staticmethod
#     def find_coins(coins: List[int], amount: int) -> int:
#
#         min_sum = amount
#         coin = coins.pop()
#         if len(coins) == 0:
#             if amount % coin == 0:
#                 return int(amount / coin)
#             else:
#                 return None
#         i = amount // coin
#         while coin * i >= 0:
#             new_change = amount - coin * i
#             # if sums.get(new_change) is None:
#             # ret_value = find_coins(coins_list[:],new_change)
#             # if ret_value is None:
#             #     i +=1
#             #     continue
#             # sums[new_change] = ret_value
#             # sums_[new_change] += 1
#             r = Solution.find_coins(coins[:], new_change)
#             if r is None:
#                 i -= 1
#                 continue
#             min_sum = min(r + i, min_sum)
#             i -= 1
#         return min_sum