def addingArr(arr1):
    arrLen = int(input("Lenght of arr:"))
    for i in range(arrLen):
        add = input("Enter Array value:")
        arr1.append(add)

def deleteArr(arr1):
    arrIndex = int(input("Enter index for delete the value:"))
    arr1.pop(arrIndex)
        
def updateArr(arr1):
    arrUpdateIndex = int(input("Enter Index:"))
    arrUpdateIndexValue = input("Enter value:")
    arr1[arrUpdateIndex] = arrUpdateIndexValue

def lenghtArr(arr1):
    arrLenght = 0
    for i in arr1:
        arrLenght = arrLenght + 1
    return arrLenght
        

def printArr(arr1):
    return arr1
   
if __name__ == "__main__":
    arr1 = []
    while True:
        print(f"1. Enter 1 for adding Array \n 2. Enter 2 for delete Array \n 3.  Enter 3 For Update array \n 4.  Enter 4 For Show Lenght array \n 5. Enter 5 For Print array")
        condition = int(input("Enter Condition:"))
        if condition == 1:
            addingArr(arr1)
        elif condition == 2:
            deleteArr(arr1)
        elif condition == 3:
            updateArr(arr1)
        elif condition == 4:
            print(f"Array Lenght:{lenghtArr(arr1)} \n")
        elif condition == 5:
            print(f"Result:{printArr(arr1)} \n")
        else:
            print("Not found")
    
