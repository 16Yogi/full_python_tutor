import string

def fun(alpha):
    i = 0 
    while i<6:
        # print(i)
        char = string.ascii_uppercase[alpha-1+i]
        j = 0
        while j<i:
            print(char,end=" ")
            j+=1
        print("")
        i+=1

if __name__ == "__main__":
    alpha = 0
    fun(alpha)