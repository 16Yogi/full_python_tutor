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
    if 1 in tup1:
        print(tup1)

if __name__ == "__main__":
    tup1 = (1,32,'fsaf',True,1)
    print(tup1)
    accessTup(tup1)