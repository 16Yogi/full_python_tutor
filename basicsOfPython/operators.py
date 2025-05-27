def arithmeticOpr(var1,var2):
    return f"Addition:{var1+var2},Substraction:{var1-var2}, multiplication:{var1*var2},dividation:{var1/var2},modulats:{var1%var2},exponention:{var1**var2},floor division:{var1//var2}"

def assingmentOpr(var1,):
    var1 = 10
    print(var1)
    var1 += 10
    print(var1)
    var1 -= 5
    print(var1)
    var1 *= 3
    print(var1)
    var1 /=2
    print(var1)
    var1 %=2
    print(var1)
    var1 //=4
    print(var1)
    var1 **=2
    print(var1)
    var1 &=1
    print(var1)
    var1 |=4
    print(var1)
    var1 ^=3
    print(var1)
    var1 >>=12
    print(var1)
    var1 <<=23
    print(var1)
    # var1 := 2

def comparisionOpr(var1,var2):
    print(var1<var2)
    print(var1>var2)
    print(var1<=var2)
    print(var1>=var2)
    print(var1!=var2)
    print(var1==var2)

def logicalOpr(var1,var2):
    if var1==var2 or var1 >=var2:
        print("var1 is equal to var2 or var1 is greater then var2")
    elif var1==var2 and var1 >= var2:
        print("var1 is equal to var2 and var1 is grater then var2")
    elif not(var1==var2):
        print("var1 is not equal to var2")

def identifyopr(var1,var2):
    print(2 is var1)
    print(1 is not var2)

def membershipOpr(var1,var2):
    print(2 in var1)
    print(1 not in var2)

def bitwiseopt(var1,var2):
    print(var1 & var2)
    print(var1 | var2)
    print(var1 ^ var2)
    print(~var2)
    print(var1 << var2)
    print(var1>>var2)
    
if __name__ == "__main__":
    var1 = int(input("First value:"))
    var2 = int(input("second value:"))
    identifyopr(var1,var2)
    membershipOpr(var1,var2)
    bitwiseopt(var1,var2)
    # var1 = 10
    # print(arithmeticOpr(var1,var2))
    # print(assingmentOpr(var1,var2))
    # print(assingmentOpr(var1))
    # print(comparisionOpr(var1,var2))
    logicalOpr(var1,var2)