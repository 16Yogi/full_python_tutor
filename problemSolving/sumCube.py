def sumCube(arr):
    n = len(arr)
    sumVal = 0
    for i in range(n):
        sumVal = sumVal + arr[i]**3
        # print(f"{sumVal}:{arr[i]**3}")
    return sumVal
if __name__ == "__main__":
    arr = [1,2,3,4]
    result = sumCube(arr)
    print(result)