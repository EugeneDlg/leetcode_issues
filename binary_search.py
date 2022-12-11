from random import randint
lst0 = []
[lst0.append(randint(0, 100)) for _ in range(5)]
lst0.sort()
print(lst0)
lst1 = []
[lst1.append(randint(0, 100)) for _ in range(5)]
lst1.sort()
print(lst1)

for i, e in enumerate(lst1):
    left_bound = 0
    right_bound = len(lst0)

    while left_bound < right_bound:
        median_index = (right_bound-left_bound) // 2
        if e == lst0[left_bound+median_index]:
            break
        elif e < lst0[left_bound+median_index]:
            right_bound -= 1
        else:
            left_bound += 1
    lst0 = lst0[:left_bound+median_index] + [e] + lst0[left_bound+median_index:]

print(lst0)