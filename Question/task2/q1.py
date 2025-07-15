def printNumber(endRange,number):
    for i in range(1,endRange+1):
        number.append(i)
    return number
        
if __name__ == "__main__":
    number = []
    endRange = int(input("Enter End Range Value:"))
    print(f"Number:{printNumber(endRange,number)}")