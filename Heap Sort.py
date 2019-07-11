def heap_sort(nos):
    global size
    size = len(nos)
    print("the size of the List is : {0} ".format(size))
    build_heap(size, nos)
    for i in range(size-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        size = size-1
        print("\n", nums)
        heapify(nos, 0, size)
    print("heap sort array:", nums)


def left_child(i):
    return 2*i+1


def right_child(i):
    return 2*i+2


def heapify(nums, i, size):
    l = left_child(i)
    print("l: ", l)
    r = right_child(i)
    print("r ", r)
    print("nums: ", nums)
    if l <= size and r <= size:
        if r != size:
            if nums[l] >= nums[r]:
                print("1")
                print("nums[l]: ", nums[l])
                print("nums[r]: ", nums[r])
                max = nums[l]
                print("max: ", max)
                max_index = l
                print("max_index: ", max_index)
            elif nums[l] <= nums[r]:
                print("2")
                print("nums[l]: ", nums[l])
                print("nums[r]: ", nums[r])
                max = nums[r]
                print("max: ", max)
                max_index = r
                print("max_index: ", max_index)
            print("i: ", i)
            print("nums: ", nums)
            if nums[i] >= max:
                print("3")
                print("nums[l]: ", nums[l])
                print("max: ", max)
                print(nums)
                return
            elif nums[i] <= max:
                print("4")
                nums[i], nums[max_index] = max, nums[i]
                print("num moi: ", nums)
                print("max_index: ", max_index)
                heapify(nums, max_index, size)
        else:
            print("5")
            nums[i], nums[l] = nums[l], nums[i]
            print(nums)


# build a heap A from an unsorted array          
def build_heap(size, elements):
    iterate = size//2-1
    print("iterate:", iterate)
    for i in range(iterate, -1, -1):
        print("In {0} iteration".format(i))
        heapify(elements, i, size)
    print("heapified array is : ", elements)


if __name__ == '__main__':
    #get input from user
    nums = [6, 9, 3, 2, 4, 1, 7, 5, 10]
    #sort the list
    heap_sort(nums)
