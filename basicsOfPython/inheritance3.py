class cl1:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def fun1(self):
        print(f"Name:{self.name}:{self.age}")

class cl2(cl1):
    def __init__(self,name,age):
        # cl1.__init__(self,name,age) 
        # super().__init__(self,name,age)
    # def __init__(self, fname, lname):
        # super().__init__(fname, lname)
        super().__init__(name,age)

if __name__ == "__main__":
    p1 = cl2("hfhdh",20)
    p1.fun1()
