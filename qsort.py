in_str = input("Enter elements to be sorted separated by commas: ")

in_list = in_str.split(",")

def qsort(in_list):
    less_list = []
    greater_list = []
    equal_list = []
    if len(in_list) > 1:
        pivot_element = in_list[len(in_list)//2]
        for e in in_list:
            e = e.strip()
            if e < pivot_element:
                less_list.append(e)
            elif e > pivot_element:
                greater_list.append(e)
            else:
                equal_list.append(e)
        return qsort(less_list) + equal_list + qsort(greater_list)
    return in_list


out_list = qsort(in_list)
[print(a) for a in out_list]