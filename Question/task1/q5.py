def factorialNumber(number):
    fact = 1
    list1 = []
    length = 0
    for i in range(1,number+1):
        fact = fact * i
        print(f"{fact} x {i} = {fact}")
        list1.append(i)
    
    for j in list1:
        length = length + 1
    return f"Result:{fact} , Length:{length}"

if __name__ == "__main__":
    number = int(input("enter nunber:"))
    print(factorialNumber(number))