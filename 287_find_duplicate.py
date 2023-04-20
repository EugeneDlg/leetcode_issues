def find_duplicates(lst):
    pointer1 = pointer2 = lst[0]
    i = 0
    while True:
        if lst[pointer1] == pointer1:
            return pointer1
        pointer1 = lst[pointer1]
        if i % 2 == 1:
            pointer2 = lst[pointer2]
            if pointer1 == pointer2:
                break
        i += 1
    pointer1 = lst[0]
    while True:
        if pointer1 == pointer2:
            return pointer1
        pointer1 = lst[pointer1]
        pointer2 = lst[pointer2]