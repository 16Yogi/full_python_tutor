def sumOfDigit(arr):
    n = len(arr)
    sumOf = arr[0]
    for i in range(1,n):
        sumOf = sumOf + arr[i]
    return sumOf

if __name__ == "__main__":
    arr = [12,41,53,2,12,5]
    result = sumOfDigit(arr)    
    print(result)