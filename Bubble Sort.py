def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [1, 77, 83, 22, 21, 5, 93, 110]
bubbleSort(arr)
for i2 in range(len(arr)):
    print("% d" % arr[i2], end=" ")
