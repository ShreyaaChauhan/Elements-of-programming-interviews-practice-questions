arr = [1, 2, 3, 4, 5, 6]


def printArr(arr, capacity=None):
    if capacity is not None:
        for i in range(capacity):
            print(arr[i])
    else:
        for i in range(len(arr)):
            print(arr[i])


printArr(arr)
