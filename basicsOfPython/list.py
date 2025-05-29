def basicList(list1):
    print(list1)
    print(len(list1))
    print(type(list1))

def accessList(list1):
    print(list1[1])
    print(list1[2:])
    print(list1[:2])
    print(list1[-1])
    print(list1[:-1])
    print(list1[:-2])
    print(list1[-2:])
    print(list1[1:3])

def changeListItem(list1):
    print(list1)
    list1[1] = "Hello Hi hI"
    print(list1)
    list1[1:3] = ["hi",121]
    print(list1)
    list1[1:3] = "yogi"
    print(list1)
    list1.insert(0,16)
    print(list1)

def addNewItem(list1,list2):
    # append(),insert(),extend()
    print(list1)
    list1.append("yogi")
    print(list1)
    list1.insert(1,"hihi")
    print(list1)
    list1.extend(list2)
    print(list1)

def removeItem(list1,list2):
    print(list1)
    list1.remove(12) #remove only one value
    print(list1)
    list2.pop()
    print(list2)
    del list1[0]
    print(list1)
    list1.clear()
    print(list1)

def LoopList(list1):
    print(list1)
    # for i in list1:
        # print(i)
    # ------------------------
    # le = len(list1)
    # for i in range(le):
    #     print(list1[i])
    # --------------------------
    # i = 0
    # while i < len(list1):
        # print(list1[i])
        # i = i+1
    # ---------------
    [print(x) for x in list1]

def listComprehension(list3):
    print(list3)
    list4 = []
    for i in list3:
        if "w" in i:
            list4.append(i)
    return list4

def sortList(list5):
    print(list5)
    list5.sort()
    print(list5)
    list5.reverse()
    print(list5)
    list5.sort(reverse = True)
    print(list5)

def listCopy(list5):
    # list6 = list5.copy()
    list6 = list5[:]
    print(list6)

def listJoin(list1,list2):
    list7 = list1+list2 
    print(list7)
    list1.extend(list2)
    print(list1)

if __name__ == "__main__":
    list1 = ["hello",12,12.32,True,12]
    list2 = [1,2,3]
    list3 = ["heafs","wef","3reaf","wfsd","iji","qk","qv"]
    list5 = [1,3,12,43,2,11,7,63]
    # print(basicList(list1))
    # accessList(list1) 
    # changeListItem(list1)
    # addNewItem(list1,list2)
    # removeItem(list1,list2)
    # LoopList(list1)
    # print(listComprehension(list3))
    # sortList(list5)
    # listCopy(list5)
    listJoin(list1,list2)

