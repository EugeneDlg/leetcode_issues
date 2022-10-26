import itertools
from itertools import permutations

from utils import verify_func


in_string = input("Enter a list to get permutations: ")
in_list = list(in_string)
elements = in_list[:]
out_list = []


def get_next_permutation(el):
    e_list = el[:]
    list0 = []
    max_el, premax_el = (e_list[1], e_list[0]) if e_list[1] > e_list[0] else (None, None)
    max_i = 1 if e_list[1] > e_list[0] else None
    elements_len = len(e_list)
    for i in range(2, elements_len):
        if e_list[i] > e_list[i - 1]:
            max_el = e_list[i]
            premax_el = e_list[i - 1]
            max_i = i
    if max_i is None:
        return None
    if max_i == elements_len - 1:
        e_list[max_i - 1], e_list[max_i] = e_list[max_i], e_list[max_i - 1]
        return e_list
    max_el_2 = max_el
    max_i_2 = max_i
    for i in range(max_i + 1, elements_len):
        if e_list[i] > premax_el:
            max_el_2 = e_list[i]
    for i in range(max_i, elements_len):
        list0.append(e_list[i])
    list0.remove(max_el_2)
    e_list[max_i - 1] = max_el_2
    list0.append(premax_el)
    list0.sort()
    return e_list[:max_i] + list0


def get_permutations():
    out_list.append(elements)
    permutation = get_next_permutation(elements)
    while permutation:
        out_list.append(permutation[:])
        permutation = get_next_permutation(permutation)


# for e in out_list:
#     print(e)
# print("Number of LGO permutations = ", len(out_list))
#
# permutations_ref = itertools.permutations(in_list)
# out_list_ref = []
# for e in permutations_ref:
#     out_list_ref.append(e)
#     print(e)
# print("Number of referenced permutations = ", len(out_list_ref))
# for i in range(0, len(out_list)):
#     if tuple(out_list[i]) != out_list_ref[i]:
#         print("Wrong element: {}".format(out_list[i]))

verify_func(get_permutations)