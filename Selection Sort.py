list = [5, 1, 4, 2, 8, 9]

mark = 0

max_index = 0
for m in range(0, len(list)):
    max = 0
    for i in range(mark, len(list)):
        print("list[i]: ", list[i])
        print("max: ", max)
        if list[i] > max:
            max = list[i]
            max_index = i
        temp = 0
        temp = list[m]
        list[m] = list[max_index]
        list[max_index] = temp
    mark = mark + 1

print(list)
