def greatThree(arr):
    n = len(arr)
    maxProduct = -10**9
    # print(maxProduct)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                maxProduct = max(maxProduct,arr[i] * arr[j] * arr[k])
    return maxProduct
    
if __name__ == "__main__":
    arr = [12,42,13,4,5]
    print(greatThree(arr))