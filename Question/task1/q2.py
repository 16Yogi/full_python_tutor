def sumOfSquare(length):
    sumSq = []
    result = 0
    for i in range(length):
        number = int(input("Enter number:"))
        sumSq.append(number)
    
    for j in sumSq:
        result = 2 * (result + j) 
        
    return f"List:{sumSq} + Result:{result}"
if __name__ == "__main__":
    length = int(input("Enter Length:"))

    print(sumOfSquare(length))