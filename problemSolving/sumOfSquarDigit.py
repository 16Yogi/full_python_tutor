def sumOfSquar(arr):
    n = len(arr)
    sumVal = 0
    
    for i in range(n):
        # sumVal = sumVal + arr[i]*2
        r = arr[i]**2
        sumVal = sumVal + r
        # print(r)
        # print(f"{sumVal} :  {arr[i]}")
    # sumVal = 
    return sumVal

if __name__ == "__main__":
    arr = [1,3,4,5,7]
    result = sumOfSquar(arr)
    print(result)