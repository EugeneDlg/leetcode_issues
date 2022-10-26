in_string = input("Enter a list to get permutations: ")
in_list = list(in_string)
elements = in_list
out_list = []


def get_permutations(out_list, elements, interim_list=[]):
    # if not elements:
    #     out_list.append(interim_list[:])
    #     return out_list
    for a in elements:
        interim_list.append(a)
        interim_elements = elements[:]
        interim_elements.remove(a)
        if not interim_elements:
            out_list.append(interim_list[:])
            interim_list.remove(a)
            return out_list
        get_permutations(out_list, interim_elements, interim_list)
        interim_list.remove(a)


lst = get_permutations(out_list, elements)
for x in out_list:
    print(x)
