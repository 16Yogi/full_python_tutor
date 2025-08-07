class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def printName(self):
        print(f"Result:{self.name}:{self.age}")

p1 = Person("Ramu",20)
# print(p1)    
p1.printName()

if __name__ == "__main__":
    print("Hello")
    # print(p1)
