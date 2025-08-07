class cl1:
    def __init__(self,name,age,add):
        self.name = name 
        self.age = age 
        self.add = add 
    
    def fun1(self):
        list1 = [self.name,self.age,self.add]
        it1 = iter(list1)
        print(next(it1))
        print(next(it1))
        print(next(it1))

class cl2(cl1):
    def __iter__(self):
        self.a = 1 
        return self
    
    def __next__(self):
        x = self.a 
        self.a += 1 
        return x

    
if __name__ == "__main__":
    # print("Hello")
    p1 = cl1("Ramu",20,"Rajghar")
    p1.fun1()

    p2 = cl2("Ramghar","fdaf","fsdf")
    p2 = iter(p2)

    print(next(p2))
    print(next(p2))
    print(next(p2))
    # print(next(p2))
