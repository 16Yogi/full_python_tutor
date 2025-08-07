import string
def fun(alpha):
    char = string.ascii_uppercase[:alpha]
    # print(char)
    for i in range(3):
        for j in char:
            print(j,end=" ")
        print("")
if __name__ == "__main__":
    alpha = 3
    fun(alpha)