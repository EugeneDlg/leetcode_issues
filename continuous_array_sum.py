from random import randint, choice

from utils import verify_func


max_length = 10
max_value = 1000


class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = max(nums)
        if max_sum <= 0:
            return max_sum
        max_sum = first_el = 0
        while len(nums):
            e = nums.pop(0)
            if e <= 0 and first_el <= 0:
                first_el = 0
                continue
            if max_sum == 0:
                max_sum = e
                first_el = e
                continue
            first_el += e
            if first_el > max_sum:
                max_sum = first_el
            if first_el < 0:
                first_el = 0
        return max_sum


class Solution2:
    def maxSubArray(self, nums) -> int:
        # max_sum = max(nums)
        # if max_sum <= 0:
        #     return max_sum
        max_sum = local_sum = nums[0]
        for e in nums[1:]:
            local_sum = max(e, local_sum + e)
            max_sum = max(max_sum, local_sum)
        return max_sum


def true_bf(ingress_list):
    max_sum = max(ingress_list)
    if max_sum <= 0:
        return max_sum
    length = len(ingress_list)
    max_sum = 0
    two_el_sum = 0
    for i0 in range(0, length):
        for i1 in range(i0, length):
            two_el_sum += ingress_list[i1]
            if two_el_sum > max_sum:
                max_sum = two_el_sum
        two_el_sum = 0
    return max_sum


def generate_sequence(rounds=10):
    ingress_list = []
    for _ in range(rounds):
        long_subseq = choice([True, False])
        if long_subseq:
            subseq_length = randint(1, max_length)
            subseq = [randint(-max_value, max_value) for _ in range(subseq_length)]
        else:
            subseq = [randint(-max_value, max_value)]
        ingress_list += subseq
    return ingress_list


ingress_list = generate_sequence(1000)
# ingress_list = ingress_list_

# print(ingress_list)
# print(Solution2().maxSubArray(ingress_list.copy()))
# print(true_bf(ingress_list.copy()))

print(verify_func(Solution().maxSubArray, ingress_list.copy()))
print(verify_func(Solution2().maxSubArray, ingress_list.copy()))
print(verify_func(true_bf, ingress_list.copy()))

