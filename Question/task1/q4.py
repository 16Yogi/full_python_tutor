def reverseNum(length):
    list1 = []
    list2 = []
    sumOfLen = 0
    myindex = 0
    for i in range(length):
        number = int(input(f"Enter nuMber {i}:"))
        list1.append(number)
    listLen = len(list1)

    for j in range(listLen):
        sumOfLen = sumOfLen + j
    
    myindex = sumOfLen
    for k in range(sumOfLen):
        myindex = myindex - 1
        list2.append(list1[myindex])
    return f"result: {list1}, index:{myindex}, sum:{sumOfLen}, reverse :{list2}"

if __name__ == "__main__":
    length = int(input("enter length:"))
    print(reverseNum(length))