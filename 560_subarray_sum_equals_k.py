from collections import defaultdict


def find_subarray_optimal(nums, k):
    currsum_dict = defaultdict(int)
    currsum = 0
    subarray_number = 0
    for e in nums:
        currsum += e
        if currsum == k:
            subarray_number += 1
        subarray_number += currsum_dict[currsum - k]
        currsum_dict[currsum] += 1
    return subarray_number