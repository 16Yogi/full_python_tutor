def search(arr,x,N):
    for i in range(N):
        if arr[i] == x:
            return i
    return -1 
if __name__ == "__main__":
    arr = [1,232,12,312,12,42,12]
    x = int(input("Enter a number:"))
    N = len(arr)
    result = search(arr,x,N)
    if(result==-1):
        print(f"Element is not present in the arry:{x}")
    else:
        print(f"Element is present in the array:{x}")
