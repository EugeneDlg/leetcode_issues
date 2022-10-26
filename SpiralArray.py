print("Here a spiral consisted of digits will be shown:")
x_dimension = int(input("Input number of columns: "))
y_dimension = int(input("Input number of rows: "))
max_len = len(str(x_dimension*y_dimension))
initial_list = list()
temp = list()
ph = '+'
temp = [ph for i in range(x_dimension)]
for i in range(y_dimension):
    initial_list.append(temp[:])
a0 = 0
a1 = -1
iterator = 0
fl = 0
shift = {"right": [0, 1],
         "down": [1, 0],
         "left": [0, -1],
         "up": [-1, 0]
}
direction = "right"
while True:
    if direction == "right" and a1 == x_dimension-1 or direction == "down" and a0 == y_dimension-1 or \
            direction == "left" and a1 == 0:
        next_element = "-"
        fl += 1
    else:
        next_element = initial_list[a0 + shift[direction][0]][a1 + shift[direction][1]]
        if next_element != ph:
            fl += 1
        else:
            fl = 0
            iterator += 1
            a0 += shift[direction][0]
            a1 += shift[direction][1]
            initial_list[a0][a1] = f"{iterator:0{max_len}d}"
            continue
    if fl > 2:
        break
    if direction == "right" and fl > 0:
        direction = "down"
        fl += 1
    elif direction == "down" and fl > 0:
        direction = "left"
        fl += 1
    elif direction == "left" and fl > 0:
        direction = "up"
        fl += 1
    elif direction == "up" and fl > 0:
        direction = "right"
        fl += 1

[print(x) for x in initial_list]