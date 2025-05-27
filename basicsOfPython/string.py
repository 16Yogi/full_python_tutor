def onlyString(var1):
    print(var1)
    print(type(var1))
    for i in var1:
        print(i)
    print(len(var1))
    print("h" in var1)
    print("a" not in var1)

def slicingFun(var1):
    print(var1[0:3]) 
    print(var1[:5]) #it not print last index value, print start index to second last targeted index
    print(var1[-1:-3]) #it not print because traverse left to right that's why
    print(var1[-3:-1])
    print(var1[3:]) #it start from 3 index to last index
    print(var1[-1:])
    print(var1[:-1])

def modifystring(var1):
    print(var1)
    print(var1.upper())
    print(var1.lower())
    print(var1.strip())
    print(var1.replace("H","MM"))
    print(var1.split(","))

def concatinate(var1,var2):
    return var1+var2

def escapeChar(var1):
    txt = "hello jhfd d fsdj \"helasd\" asdas"
    print(txt)
    return var1
if __name__ == "__main__":
    var1 = input("Enter:")
    # var2 = input("Enter:")
    # onlyString(var1)
    # slicingFun(var1)
    # modifystring(var1)
    # print(concatinate(var1,var2))
    print(escapeChar(var1))