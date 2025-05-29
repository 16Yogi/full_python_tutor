def thirdLargestNumber(arr):
    n = len(arr)
    arr.sort()
    print(arr)
    for i in range(n-2,-1,-1):
        if arr[i] != arr[n-2]:
            return arr[i]

def thirdLarg(arr):
    n = len(arr)
    arr.sort()
    return arr[n-3]
        
if __name__ == "__main__":
    arr = [12,34,1,4,12,4,123,446,72,45]
    # print(thirdLargestNumber(arr))
    print(thirdLarg(arr))