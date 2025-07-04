def basicLoop(i,l):
    result = []
    for i in range(1,l):
        result.append(i)
    return result

def breakContinue(i,l):
    result = []
    for i in range(1,l):
        if i == 2:
            break
        result.append(i)
    return result

def nested(i,l):
    for i in range(1,l):
        for j in range(2,l):
            return f"{i} : {j}"
        
if __name__ == "__main__":
    print("for loop")
    i = int(input("Start point:"))
    l = int(input("End point:"))
    # result = basicLoop(i,l)
    result = nested(i,l)
    print(result)

    for i in range(1,10):
        for j in range(1,10):
            print(i*j,end=" ")
        print()