def basicSet(set1):
    print(f"Set: {set1}")
    print(type(set1))
    # print(len(set))

def accessSet(set1):
    for i in set1:
        print(i)
    print(set1)
    print("ramlal" in set1)
    print("ramlal" not in set1)

def addSet(set1,set2):
    set1.add("Mohan Payre")
    print(set1)
    print(set2)
    set1.update(set2)
    print(set1)

def removeSet(set1,set2):
    # remove discard pop clear del
    set2.remove("a")
    print(set2)
    set2.discard("b")
    print(set2)
    set1.pop()
    print(set1)
    # del set1 
    # print(set1)
    set2.clear()
    print(set2)

def loopSet(set1,set2):
    for i in set2:
        print(i)

def joinSet(set,set2):
    set3 = set1.union(set2)
    print(set3)
    set4 = set1 | set2 
    print(set4)
    set5 = set1.intersection(set2)
    print(set5)
    set6 = set1 & set2 
    print(set6)
    set1.intersection_update(set2)
    print(set1)
    set7 = set1.difference(set2)
    print(set7)
    set8 = set1-set2 
    print(set8)
    set1.difference_update(set2)
    print(set1)
    set9 = set1.symmetric_difference(set2)
    print(set9)
    set10 = set1 ^ set2 
    print(set10)
    set1.symmetric_difference_update(set2)
    print(set1)

if __name__ == "__main__":
    set1 = {"ramlal",18,5.2,True,"ramlal"}
    set2 = {"a","b","c"}
    # basicSet(set1)
    # accessSet(set1)
    # addSet(set1,set2)
    # removeSet(set1,set2)
    # loopSet(set1,set2)
    joinSet(set1,set2)