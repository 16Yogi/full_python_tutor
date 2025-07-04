def ifelfun(val):
    if val >= 18:
        if val >= 25 and val <=30:
            print("tumhari to cut gae")
        elif val >= 18 and val <= 25:
            print("study kr le bsdk")
        elif val >= 30 and val<=40:
            print("tu yaha ky kr raha bsdk")
        elif val >=40:
            print("Abe chala js bsdk")
        else:
            print("G**d mar gae")    
    elif val<=17:
        if val >= 17 and val <= 15:
            print("Bsdk abhi abhi ande se bahar aya hai") 
        elif val >=10 and val <= 11:
            print("abe, thodi to sharam kr le")
        elif val <=9:
            print("tu to bahut data ho gya yr")
        else:
            print("Sorry yr teko ko kuch nahi bol sakta")
    else:
        print("Abe kaha se aya hai tu")
if __name__ == "__main__":
    print("Kisko girlfriend chahiye")
    print("*****************************************")
    val = int(input("age:"))
    # print(ifelfun(val))
    ifelfun(val)
    print("Hello") if val <=10 else print("sorry")