import string 
def fun(alpha):
    result = 0
    for i in range(0,6):
        result = alpha - i
        char = string.ascii_lowercase[:result]
        for j in char:
            print(j,end=" ")
        print(" ")
if __name__ == "__main__":
    alpha = 5
    fun(alpha)