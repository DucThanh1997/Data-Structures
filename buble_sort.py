unsorted_list = [5, 1, 4, 2, 8, 9]
i = 0
j = 0

for x in range(0, len(unsorted_list)-i):
    print("unsorted_list[x]: ", unsorted_list[x])
    m = 0
    for y in range(1, len(unsorted_list)-i):
        print("y: ", y)
        if unsorted_list[m] > unsorted_list[y]:
            temp = 0
            temp = unsorted_list[m]
            unsorted_list[m] = unsorted_list[y]
            unsorted_list[y] = temp
            print("unsorted_list: ", unsorted_list)
        m = m + 1
    i = i + 1

print(unsorted_list)

# độ phức tạp n*n
