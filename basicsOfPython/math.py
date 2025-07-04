def basicMath(a):
    match a:
        case 1:
            return "hello"
        case 2:
            return "hi"
        case 3:
            return "hiii"
        case 4:
            return "HEllo hi"
        case 5:
            return "Chalo"
        case _:
            return f"not match"

def basicMath2(a):
    match a:
        case 1:
            return "Helo"
        case 2|3|4:
            return "Hello chalo"
        case _:
            return "Not match"

def basicMath3(a):
    match a:
        case 1:
            return "Hello"
        case 2|3|4|5:
            return "Chaloooo"
        case 6|7|8 if a == 8:
            return f"{a} available"
        case _: 
            return "not available"
        
if __name__ == "__main__":
    # print("Math")
    a = int(input("enter:"))
    # result = basicMath(a)
    # result = basicMath2(a)
    result = basicMath3(a)
    print(result)
    