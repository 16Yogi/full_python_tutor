def sumOfPre(arr):
    n = len(arr)
    sumPre = [0] * n
    sumPre[0] = arr[0]
    for i in range(1,n):
        sumPre[i] = sumPre[i-1]+ arr[i]
    return sumPre
if __name__ == "__main__":
    arr = [1,34,16,45,9,12]
    sumPre = sumOfPre(arr)
    for i in sumPre:
        print(i,end=" ")