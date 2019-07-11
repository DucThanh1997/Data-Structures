list = [5, 1, 4, 2, 8, 9]

mark = 1

for i in range(0, len(list)):
    print("\n")
    print("\n")
    print("i: ", i)
    for m in range(0, mark):
        print("m: ", m)
        print("mark: ", mark)
        print("list[m]: ", list[m])
        print("list[i]: ", list[i])
        if list[i] > list[m]:
            temp = 0
            temp = list[i]
            list[i] = list[m]
            list[m] = temp
        print("list: ", list)
    mark = mark + 1
print(list)

