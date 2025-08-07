class cl1:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def fun1(self):
        print(f"{self.name}:{self.age}")

class cl2(cl1):
    def __init__(self,name,age):
        # cl1.__init__(self,name,age)
        super().__init__(name,age) 
        self.test 


if __name__ == "__main__":
    # print("Hello")
    p1 = cl2("mohan",30)
    p1.fun1()