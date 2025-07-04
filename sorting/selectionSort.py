def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i 
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j 
        arr[i],arr[min_index] = arr[min_index], arr[i]
def print_array(arr):
    for val in arr:
        print(val,end=" ")
    print()
if __name__ == "__main__":
    arr = [12,42,1,56,98,89]
    print("Original array:",end="")
    print_array(arr)
    selection_sort(arr)
    print("sorted array:",end="")
    print_array(arr)