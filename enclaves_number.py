from typing import List
from collections import deque


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        x_len = len(grid[0])
        y_len = len(grid)
        total_earth = sum(map(sum, grid))
        cells = deque()
        perimeter = [[[0, 0], [0, 1]], [[0, x_len - 1], [1, 0]], [[y_len - 1, 0], [0, 1]], [[0, 0], [1, 0]]]
        adjacent_count = 0
        for j in perimeter:
            start_y = j[0][0]
            start_x = j[0][1]
            incr_y = j[1][0]
            incr_x = j[1][1]
            x_perimeter = start_x
            y_perimeter = start_y
            while x_perimeter < x_len and y_perimeter < y_len:
                y = y_perimeter
                x = x_perimeter
                if grid[y][x]:
                    cells.appendleft((y, x))
                    while len(cells):
                        adjacent_count += 1
                        y, x = cells.pop()
                        if x + 1 < x_len and grid[y][x + 1] and (y, x + 1) not in cells:
                            cells.appendleft((y, x + 1))
                        if y + 1 < y_len and grid[y + 1][x] and (y + 1, x) not in cells:
                            cells.appendleft((y + 1, x))
                        if x - 1 >= 0 and grid[y][x - 1] and (y, x - 1) not in cells:
                            cells.appendleft((y, x - 1))
                        if y - 1 >= 0 and grid[y - 1][x] and (y - 1, x) not in cells:
                            cells.appendleft((y - 1, x))
                        grid[y][x] = 0
                y_perimeter += incr_y
                x_perimeter += incr_x
        return total_earth - adjacent_count