def shellSort(arr): 

    n = len(arr) 
    gap = n/2
    print("gap: ", gap)
    while gap > 0:
        for i in range(int(gap), n):
            print("i: ", i)
            print("arr[i]: ", arr[i])
            temp = arr[i]
            j = i 
            while j >= int(gap) and arr[j-int(gap)] >temp:
                arr[j] = arr[j-int(gap)]
                j -= int(gap)
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap = int(gap)/2

if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3]

    n = len(arr)
    print("Array before sorting:")
    for i in range(n):
        print(arr[i])

    shellSort(arr)

    print("\nArray after sorting:")
    for i in range(n):
        print(arr[i])
