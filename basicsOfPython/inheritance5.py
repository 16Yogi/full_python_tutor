class cl1:
    def __init__(self,name,age):
        print("Hello") 
        self.name = name 
        self.age = age 

    def fun1(self):
        print(f"{self.name}:{self.age}")

class cl2(cl1):
    def __init__(self,name,age):
        super().__init__(name,age)
        print("Cl22")
        self.test = "mohandfsdfsf"
if __name__ == "__main__":
    # p1 = cl1("mohan",23)
    # p1.fun1()
    p2 = cl2("ramu",3232)
    p2.fun1()
    print(p2.test)
    
