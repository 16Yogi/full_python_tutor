def RevrasValue(number,endNumber,length,reversed ):
    
    for i in range(1,endNumber+1):
        number.append(i)
    print(number)

    for j in number:
        length = length + 1
    print(length)
    
    for k in range(length):
        # print(length)
        length  = length -1
        reversed.append(number[length])
        # length = length - 1 
    return f"Right:{number} - Reversed:{reversed}"
         


if __name__ == "__main__":
    number = []
    reversed = []
    length = 0
    endNumber = int(input("Enter End number:"))
    print(RevrasValue(number,endNumber,length,reversed))