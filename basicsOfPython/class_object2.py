# class Person:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age
# p1 = Person("Mohan",30) 

# class Person2:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age

#     def __str__(self):
#         return f"{self.name}({self.age})" 
# p2 = Person2("Shayam",30)


# class Person3:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 
    
#     def fun1(self):
#         print(f"Hello:{self.name}:{self.age}")

# p3 = Person3("Mohan",34)
# p3.fun1() 

# if __name__ == "__main__":
#     print("Class object 2")
#     print("--------------------------")
#     print(p1)
#     print(p2)
#     print(p3)


class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        print("init")
    
    def fun(self):
        return f"{self.name},{self.age}"
p1 = Person("Hello",20)

print(p1.fun())


if __name__ == "__main__":
    print("main")