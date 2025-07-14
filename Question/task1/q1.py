def sumOf(length):
    sumList = []
    sum = 0
    for i in range(length):
        num1 = int(input(f"Enter index {i} number:"))
        sumList.append(num1)
    
    for j in sumList:
        #print(j)
        sum = sum+j
    return f"MyList:{sumList} + Total of List :{sum}"
if __name__ == "__main__":
    # print("hello")
    length = int(input("Enter Length:"))
    #num1 = int(input("Enter number:"))

    print(sumOf(length))
