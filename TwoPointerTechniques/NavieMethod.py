def two_sum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return True
    return False

arr = [12,6,23,89,234,53]
# target = -2
target = int(input("Target:"))

if two_sum(arr,target):
    print("True")
else:
    print("False")