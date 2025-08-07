import string 

def alphaNumber(alpha):
    for i in range(0,6):
        alpha = i 
        # print(alpha)
        char = string.ascii_lowercase[:alpha]
        for j in char:
            print(j,end=" ")
        print(" ")

if __name__ == "__main__":
    # print("Hello")
    alpha = 0
    # print(alphaNumber(alpha))
    alphaNumber(alpha)