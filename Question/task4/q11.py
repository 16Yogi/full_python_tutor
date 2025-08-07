import string
# def charALpha():
#     # print("Hello")
#     res = string.ascii_lowercase
#     print(res)

def charAlpha(a):
    # res = string.ascii_lowercase[:a]
    # return res
    var1 = string.ascii_lowercase[:a]
    for i in range(3):
        for j in var1:
            print(j,end=" ")
        print(" ")
        

if __name__ == "__main__":
    a = 3
    # print(charAlpha(a))
    charAlpha(a)