def sumOfCube(length):
    list1 = []
    result = 0
    for i in range(length):
        number = int(input(f"Enter number {i}:"))
        list1.append(number)
    for j in list1:
        result = 3*(result + j) 
    return f"List: {list1} + Result : {result}"
if __name__ == "__main__":
    length = int(input("Enter lenght:"))
    print(sumOfCube(length))