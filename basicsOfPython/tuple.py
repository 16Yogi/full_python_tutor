def basic(tup1):
    print(tup1)
    print(type(tup1))
    print(len(tup1))

def accessTup(tup1):
    print(tup1[1])
    print(tup1[2:3])
    print(tup1[-1])
    print(tup1[1:])
    print(tup1[:3])
    print(tup1[:-1])
    print(tup1[-2:])
    print(tup1[-2:-1])
    print(tup1[-1:-3])
    if 1 in tup1:
        print(tup1)

def updateTup(tup1):
    list1 = list(tup1)
    list1[1] = "Hello ramla"
    tup1 = tuple(list1)
    print(tup1)
    list1 = list(tup1)
    list1.append("mohan payare")
    tup1 = tuple(list1)
    print(tup1)
    list1 = list(tup1)
    list1.remove(1)
    tup1 = tuple(list1)
    print(list1)
    del tup1
    print(tup1)

def unpackTup(tup2):
    print(tup2)
    (a,b,c,d,e) = tup2 
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    (aa,bb,*cc) = tup2
    print(aa)
    print(bb)
    print(cc) 
    (aa,*bb,cc) = tup2 
    print(aa)
    print(bb)
    print(cc)

def loopTup(tup2):
    for i in tup2:
        print(i)
    print("------------------")
    for j in range(len(tup2)):
        print(tup2[j])
    print("-------------------")
    k = 0 
    while k < len(tup1):
        print(tup1[k])
        k= k+1

def joinTup(tup2,tup1):
    result = tup1 + tup2 
    print(result)
    tup3 = tup1*2
    print(tup3)
    
if __name__ == "__main__":
    tup1 = (1,32,'fsaf',True,1)
    tup2 = ("a","b","c","d","e")
    # print(tup1)
    # accessTup(tup1)
    # updateTup(tup1)
    # unpackTup(tup2)
    # loopTup(tup2)
    joinTup(tup1,tup2)