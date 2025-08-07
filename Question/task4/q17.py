import string

def fun(alpha):
    i = 1
    while i<=5:
        char = string.ascii_uppercase[alpha-1+i]
        j = 1
        k = 5
        while j <= k:
            print(char,end=" ")
            j+=1
        print(" ")
        i+=1

if __name__ == "__main__":
    alpha = 0 
    fun(alpha)