# class cl1:
#     def __init__ (self,name,age):
#         self.name = name 
#         self.age = age

#     def fun1(self):
#         print(f"{self.name}:{self.age}")

# class cl2(cl1):
#     def __init__(self,name,age):
#         cl1.__init__(self,name,age)

# p2 = cl2("mohan",20)
# p2.fun1()

# if __name__ == "__main__":
#     print("Main")



class cl1:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def fun1(self):
        print(f"{self.name}:{self.age}")

class cl2(cl1):
    def __init__(self,name,age):
        cl1.__init__(self,name,age)
        
if __name__ == "__main__":
    p2 = cl2("Mohan",300)
    p2.fun1()