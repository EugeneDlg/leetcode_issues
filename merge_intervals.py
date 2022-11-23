from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_dict = {}
        for e in intervals:
            lower_el = e[0]
            upper_el = e[1]
            intervals_dict[lower_el] = max(intervals_dict[lower_el], upper_el) \
                if intervals_dict.get(lower_el) else upper_el
        sorted_list = self.my_qsort(list(intervals_dict.keys()))

        merged_list = []
        if len(sorted_list) == 1:
            return [[sorted_list[0], intervals_dict[sorted_list[0]]]]
        base_el = sorted_list[0]
        # merged_list.append((base_el, intervals_dict[base_el]))
        max_upper_bound = intervals_dict[base_el]
        for e in sorted_list[1:]:
            if e > max_upper_bound:
                merged_list.append((base_el, max_upper_bound))
                base_el = e
                max_upper_bound = intervals_dict[base_el]
            else:
                max_upper_bound = max(max_upper_bound, intervals_dict[e])
        merged_list.append((base_el, max_upper_bound))
        return merged_list

    def my_qsort(self, sort_list):
        if len(sort_list) <= 1:
            return sort_list
        lower_list = []
        upper_list = []
        equal_list = []
        for i, e in enumerate(sort_list):
            base_index = len(sort_list) // 2
            base_el = sort_list[base_index]
            if e < base_el:
                lower_list.append(e)
            if e > base_el:
                upper_list.append(e)
            if e == base_el:
                equal_list.append(e)
        return self.my_qsort(lower_list) + equal_list + self.my_qsort(upper_list)

