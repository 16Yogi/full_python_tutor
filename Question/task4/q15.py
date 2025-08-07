import string
# def fun(alpha):
#     for i in range(6):
#         alpha = i
#         char = string.ascii_uppercase[:alpha]
#         for j in char:
#             print(j,end=" ")
#         print("")
    # print(char)

def fun(alpha):
    i = 0 
    while i < 3:
        j = 0 
        char = string.ascii_uppercase[alpha - 1 + i]
        while j < 3:
            print(char,end=" ")
            j+=1 
        print()
        i+=1
if __name__ == "__main__":
    alpha = 1
    fun(alpha)