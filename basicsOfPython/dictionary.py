def basicDict(dict1):
    print(dict1)
    print(dict1['age'])
    print(len(dict1))
    print(type(dict1))
    dict2 = dict(name="mohan",age=20,add='hyd')
    print(dict2)
    print(type(dict2))

def accessDict(dict1):
    print(dict1)
    # print(dict1[1])
    print(dict1['name'])
    print(dict1.get('age'))
    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())

def changeDict(dict1):
    dict1['name'] = 'Mohan Payare'
    print(dict1)
    dict1.update({"age":100})
    print(dict1)

def addDict(dict1):
    dict1['class'] = 'pata nahi'
    print(dict1)
    dict1.update({"papa name":"Papa"})
    print(dict1)

def removeDict(dict1):
    # dict1.pop("add")
    print(dict1)
    # dict1.popitem()
    # print(dict1)
    del dict1['add']
    print(dict1)
    dict1.clear()
    print(dict1)

def loopDict(dict1):
    # for i in dict1:
        # print(i)
        # print(dict1[i])
        # print(f"{i}:{dict1[i]}")
    # for i in dict1.keys():
    #     print(i)
    # for i in dict1.values():
    #     print(i)
    for i in dict1.items():
        print(i)

def copyDict(dict1):
    dict2 = dict1.copy()
    print(dict2)
    dict3 = dict(dict1)
    print(dict3)

def nestedDict():
    dict2 = {
        "stu1":{
            "name":"ramu",
            "year":"2022"
        },
        "stu2":{
            "name":"mohan",
            "year":"2024"
        },
        "stu3":{
            "name":"Geeta",
            "year":"2026"
        }
    }
    print(dict2)

if __name__ == "__main__":
    dict1 = {
        "name":"Ramu",
        "age":20,
        "add":"I don't know"
    }
    # basicDict(dict1)
    # accessDict(dict1)
    # changeDict(dict1)
    # addDict(dict1)
    # removeDict(dict1)
    # loopDict(dict1)
    # copyDict(dict1)
    nestedDict()
