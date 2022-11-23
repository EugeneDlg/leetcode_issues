import os
import math
import datetime
import re


####################################
def compare_strings():
    a = input()
    b = input()
    a_dict = {}
    output = ["I"] * len(a)

    def hide_loop(m):
        a_dict[m][2] += 1
        if len(a_dict[m][0]) > a_dict[m][2]:
            a_dict[m][1] = a_dict[m][0][a_dict[m][2]]
        else:
            a_dict[m][1] = -1
    for i, e in enumerate(a):
        if a[i] == b[i]:
            continue
        if a_dict.get(e):
            a_dict[e][0].append(i)
        else:
            a_dict[e] = [[], [], []]
            a_dict[e][0] = [i]
            a_dict[e][1] = i
            a_dict[e][2] = 0
    for i, e in enumerate(b):
        if a[i] == b[i]:
            output[i] = "P"
            continue
        if a_dict.get(e) is None:
            continue
        else:
            q = a_dict[e][1]
            if q == -1:
                continue
            if a[q] != b[q]:
                output[i] = "S"
                hide_loop(e)
    print("".join(output))


#####################################
def custom():
    filename = "input3.txt"
    with open(filename, "r") as file:
        in_str = file.read()
    # in_str = input()
    output_list = []
    in_list = in_str.split("\n")
    if in_list[len(in_list) - 1] == "":
        in_list.pop()
    for e in in_list[1:]:
        m = re.search(r"(NAME_CONTAINS|PRICE_LESS_THAN|PRICE_GREATER_THAN|DATE_AFTER|DATE_BEFORE)\s+(.+)", e)
        if m.group(1) == "NAME_CONTAINS":
            name_crit = m.group(2).lower()
        if m.group(1) == "PRICE_LESS_THAN":
            prise_l_crit = int(m.group(2))
        if m.group(1) == "PRICE_GREATER_THAN":
            prise_g_crit = int(m.group(2))
        if m.group(1) == "DATE_AFTER":
            date_a_crit = datetime.datetime.strptime(m.group(2), "%d.%m.%Y")
        if m.group(1) == "DATE_BEFORE":
            date_b_crit = datetime.datetime.strptime(m.group(2), "%d.%m.%Y")

    json_list = in_list[0].split("{")
    json_list[len(json_list) - 1] = json_list[len(json_list) - 1].strip()
    json_list[len(json_list) - 1] = json_list[len(json_list) - 1].rstrip("]")
    json_list[len(json_list) - 1] = json_list[len(json_list) - 1].rstrip(",") + ","
    for e in json_list:
        if len(e) < 2:
            continue
        e = e.strip()
        m = re.search(r"\"name\"\s*:\s*\"([\w\s]+)\"", e)
        if re.search(name_crit, m.group(1), flags=re.IGNORECASE) is None:
            continue
        m = re.search(r"\"price\"\s*:\s*(\d+)", e)
        price = int(m.group(1))
        if price > prise_l_crit or price < prise_g_crit:
            continue
        m = re.search(r"\"date\"\s*:\s*\"([\d.]+)\"", e)
        date = datetime.datetime.strptime(m.group(1), "%d.%m.%Y")
        if date > date_b_crit or date < date_a_crit:
            continue
        m = re.search(r"\"id\"\s*:\s*(\d+)", e)
        id = int(m.group(1))
        output_list.append([])
        output_list[len(output_list) - 1].append(id)
        output_list[len(output_list) - 1].append("{" + e)

    if len(output_list) > 0:
        output_list.sort(key=lambda x: x[0])
        output_list[0][1] = "[" + output_list[0][1]
        output_list[len(output_list) - 1][1] = output_list[len(output_list) - 1][1].strip().rstrip(",") + "]"
        # print("".join([x[1] for x in output_list]))
        with open("output.txt", "w") as file:
            file.write("".join([x[1] for x in output_list]))
    else:
        with open("output.txt", "w") as file:
            file.write("")


#################################################
def escape_plan():
    nm = input()
    n_len, m_len = list(map(int, nm.split()))
    n = []
    for _ in range(n_len):
        n.append(input())
    plan = []
    s_coor = []
    space_num = 0
    for i0, e0 in enumerate(n):
        plan.append([])
        for i1, e1 in enumerate(e0):
            plan[i0].append(e1)
            if e1 == "S":
                s_coor.append(i0)
                s_coor.append(i1)
            if e1 == ".":
                space_num += 1

    shift = [[]]
    shift[0].append(-1)
    shift[0].append(0)
    shift.append([])
    shift[1].append(0)
    shift[1].append(-1)
    shift.append([])
    shift[2].append(1)
    shift[2].append(0)
    shift.append([])
    shift[3].append(0)
    shift[3].append(1)
    escape_temp = []
    i = 0
    escape_temp.append(s_coor)
    while i < len(escape_temp):
        x, y = escape_temp[i]
        for e in shift:
            x_neighb = x + e[0]
            y_neighb = y + e[1]
            if x_neighb > n_len - 1 or x_neighb < 0 or y_neighb > m_len - 1 or y_neighb < 0:
                continue
            if plan[x_neighb][y_neighb] != ".":
                continue
            if x_neighb - x < 0:
                plan[x_neighb][y_neighb] = "D"
            if x_neighb - x > 0:
                plan[x_neighb][y_neighb] = "U"
            if y_neighb - y < 0:
                plan[x_neighb][y_neighb] = "R"
            if y_neighb - y > 0:
                plan[x_neighb][y_neighb] = "L"
            escape_temp.append([x_neighb, y_neighb])
        i += 1
    for e in plan:
        print("".join(e))


#################################
def cloud_calc():
    filename = "input4.txt"
    # input_str = "}"*10_000_000
    # with open(filename, "w") as file:
    #     file.write(input_str)

    filename_size = os.path.getsize(filename)
    chunk_size = 5_000_000
    stack = []
    closing_min = 0
    parenth = 0
    # t0 = time.perf_counter()
    with open(filename, "r") as file:
        for _ in range(math.ceil(filename_size/chunk_size)):
            in_str = file.read(chunk_size)
            p = file.tell()
            file.seek(p)
            for i, e in enumerate(in_str):
                if e == "{":
                    stack.append([])
                    stack[len(stack) - 1].append("{")
                    stack[len(stack) - 1].append(i)
                if e == "}":
                    if closing_min == 0:
                        closing_min = i + 1
                    if len(stack) > 0 and stack[len(stack)-1] == "{":
                        stack.pop()
                        continue
                    else:
                        stack.append([])
                        stack[len(stack) - 1].append("}")
                        stack[len(stack) - 1].append(i)
                if len(stack) == 2 and e == "}":
                    parenth = -1
                    break
            if parenth == -1:
                break
    if len(stack) != 1:
        parenth = -1
    else:
        if stack[0][0] == "{":
            parenth = stack[0][1] + 1
        else:
            parenth = closing_min

    # t1 = time.perf_counter()
    print(parenth)
