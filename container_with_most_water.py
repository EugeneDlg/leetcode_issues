from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left_bound = 0
        right_bound = len(height)-1
        while left_bound < right_bound:
            current_volume = min(height[left_bound], height[right_bound])*(right_bound-left_bound)
            max_volume = max(current_volume, max_volume)
            if height[left_bound] > height[right_bound]:
                right_bound -= 1
            else:
                left_bound += 1
        return max_volume