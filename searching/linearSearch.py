def search(arr,N,x):
    for i in range(N):
        if arr[i] == x:
            return arr[i]
    return -1
if __name__ == "__main__":
    arr = [12,3,1,4,12,412,6,434123,3441,76,12]
    N = len(arr)
    x = int(input("Enter a value:"))
    result = search(arr,N,x)
    if result == -1:
        print("Not present !")
    else:
        print(f"Present:{result}")