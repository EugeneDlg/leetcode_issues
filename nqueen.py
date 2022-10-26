import time
import copy


class Solution:
    queens = []

    def solveNQueens(self, n: int):
        print(n)
        Solution.n = n
        queen = "Q"
        vacant = "."
        keys = [(i, j) for i in range(0, n) for j in range(0, n)]
        pos_dict = {}
        pos_dict = pos_dict.fromkeys(keys, vacant)
        self.find_queen_positions(n, pos_dict)
        # self.find_queen_positions2(n)
        result_list = []
        # Solution.queens.sort()
        for e in Solution.queens:
            temp_list = []
            for ee in e:
                temp = [vacant for _ in range(0, n)]
                y = ee[1]
                temp[y] = queen
                temp_list.append("".join(temp))
            result_list.append(temp_list[:])
        return result_list

    def find_queen_positions(self, n, my_pos_dict, queens_temp=None):
        queens_temp = queens_temp or []
        first_x = None
        for key, value in my_pos_dict.items():
            x = key[0]
            y = key[1]
            if first_x is None:
                first_x = x
            elif x != first_x:
                break
            my_pos_dict_local = my_pos_dict.copy()
            my_pos_dict_local.pop(key)
            queens_temp.append(key)
            if len(queens_temp) == n:
                Solution.queens.append(tuple(sorted(queens_temp)))
                queens_temp.pop()
                continue

            for i in range(1, n):
                key = ((x + i) % n, y)
                if my_pos_dict_local.get(key) is not None:
                    my_pos_dict_local.pop(key)
            for i in range(1, n):
                key = (x, (y + i) % n)
                if my_pos_dict_local.get(key) is not None:
                    my_pos_dict_local.pop(key)
            diff = abs(x - y)
            min_xy = min(x, y)
            modus = n - diff
            for i in range(1, modus):
                shift_x = (x > y) * diff + (min_xy + i) % modus
                shift_y = (y > x) * diff + (min_xy + i) % modus
                key = (shift_x, shift_y)
                if my_pos_dict_local.get(key) is not None:
                    my_pos_dict_local.pop(key)
            modus = n - abs(x - (n - 1 - y))
            sum_xy = x + y
            diff = sum_xy - n + 1
            for i in range(1, modus):
                shift_x = (x - (diff > 0) * diff + i) % modus + (diff > 0) * diff
                shift_y = sum_xy - shift_x
                key = (shift_x, shift_y)
                if my_pos_dict_local.get(key) is not None:
                    my_pos_dict_local.pop(key)
            if len(my_pos_dict_local) > 0:
                self.find_queen_positions(n, my_pos_dict_local, queens_temp)
            queens_temp.pop()

    def find_queen_positions2(self, n, row_number=0, row=None, queens_temp=None):
        row = row or [[0, 0, 0] for _ in range(0, n)]
        queens_temp = queens_temp or []
        row_temp = copy.deepcopy(row)
        for i, e in enumerate(row):
            if e[1] > 0:
                row_temp[i][1] -= 1
                if i - 1 >= 0:
                    row_temp[i - 1][1] += 1
            if e[2] > 0:
                row_temp[i][2] -= 1
                if i + 1 < n:
                    row_temp[i + 1][2] += 1

        for i, e in enumerate(row_temp):
            next_row = copy.deepcopy(row_temp)
            if e[0] == 0 and e[1] == 0 and e[2] == 0:
                queens_temp.append((row_number, i))
                if len(queens_temp) == n:
                    Solution.queens.append(tuple(sorted(queens_temp)))
                    queens_temp.pop()
                    break
                next_row[i][0] = 1
                next_row[i][1] = 1
                next_row[i][2] = 1
                if row_number < n:
                    self.find_queen_positions2(n, row_number + 1, next_row, queens_temp)
                queens_temp.pop()


print(Solution().solveNQueens(4))

