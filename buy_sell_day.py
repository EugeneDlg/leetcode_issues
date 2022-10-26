days = [7, 6, 5, 20, 9, -10, 0]
# days = [100, 0, 5, 4, 6, 2, 5, 9, 0, 1, 900]
# days = [1, -1, -2]
# days = [1, 5, 10]
# days = [10, 10, 10]
# days = [0, 0, 0]
# days = [-9, -9, -9]
# days = [0]
# days = [-9, 9, -9]
# days = [-9, 9, -9, 9, -9]

def find_profit_bf(days):
    diff = []
    for i0 in range(0, len(days)):
        for i1 in range(i0+1, len(days)):
            current_diff = days[i1]-days[i0]
            diff.append(current_diff if current_diff > 0 else 0)
    return max(diff) if len(diff) > 0 else 0


def find_profit(days):
    max_profit = 0
    increasing = 0
    descending = 0
    prev_element = days[0]
    local_min = prev_element
    local_descending = 0
    for e in days[1:]:
        diff = e - prev_element
        if diff > 0:
            increasing += diff
            descending += local_descending
            max_profit = max(max_profit, increasing - descending)
            local_descending = 0
        if diff < 0:
            if e < local_min:
                local_min = e
                increasing = 0
                descending = 0
                local_descending = 0
            else:
                local_descending += -diff
        prev_element = e
    return max_profit


print(find_profit_bf(days))
print(find_profit(days))
