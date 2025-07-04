# def basicLoop(i,l):
#     while i<=l:
#         # return i
#         print(i) 
#         i+=1

def basicLoop(i,l):
    result = []
    while i<=l:
        result.append(i)
        i+=1
    return result

def continueLoop(i,l):
    result = []
    while i <= l:
        i+=1
        if i==5:
            # break
            continue
        result.append(i)
    return result



if __name__ == "__main__":
    i = int(input("Starting point:"))
    l = int(input("Ending point:"))
    # result = basicLoop(i,l)
    result = continueLoop(i,l)
    print(result)
