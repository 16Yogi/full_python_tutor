def binarySearch(arr,low,high,x):
    if high>=low:
        mid = low+(high-low)//2
        if arr[mid] == x:
            return mid 
        elif arr[mid]>x:
            return binarySearch(arr,low,mid-1,x)
        else:
            return binarySearch(arr,mid+1,high,x)
    else:
        return -1
if __name__ == '__main__':
    arr = [1,2,3,2,12,341,123,23]
    x = int(input("Enter element:"))
    result = binarySearch(arr,0,len(arr)-1,x)
    if result !=-1:
        print(f"Element is present in the array:{x}")
    else:
        print(f"Element is not present in the arrya:{x}")