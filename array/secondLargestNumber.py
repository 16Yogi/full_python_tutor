def getSecondLarge(arr):
    n = len(arr)
    arr.sort()
    for i in range(n-2,-1,-1):
        # print(arr[i])
        if arr[i] != arr[n-1]:
            return arr[i]
    return -1

if __name__ == "__main__":
    arr = [12,32,123,112,31,455,234,3,24,53]
    print(getSecondLarge(arr))