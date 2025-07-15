def eveNumber(eve,odd,allNum,rangeNum):
    for i in range(1,rangeNum+1):
        allNum.append(i)
    
    for j in allNum:
        if j%2==0:
            eve.append(j)
    
    for k in allNum:
        if k%2==1:
            odd.append(k)
    return f"- All Number:{allNum} \n- Even Number:{eve} \n- odd Number:{odd}"
if __name__ == "__main__":
    eve = []
    odd = []
    allNum = []
    rangeNum = int(input("Enter Range of number:"))
    print(eveNumber(eve,odd,allNum,rangeNum))
