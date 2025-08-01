#1.)class (it is a group of object)

# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# # del emp.id//delete the objects
# # del emp.name
# emp.display()


#2.)object(It is an identifiable entity)

# class Car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=Car("Toyota",2016)
# c1.display()


#3.)method
#1.creating the constructor(paramiterized constructor)

# class Employee:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display(self):
#         print("ID:%d\n Name:%s"%(self.id,self.name))
# emp1=Employee("John",101)
# emp2=Employee("David",102)
# emp1.display()
# emp2.display()

#2.non paramiterized constructor

# class Student:
#     def __init__(self):
#         print("this is non parametrized constructor")
#     def show(self,name):
#         print("Hello",name)
# student=Student()
# student.show("John")

    #12.) INHERITENCE
# 4.1)single inheritence(one base class and one derived class)
# class Animal:
#     def speak(self):
#         print("Animal speaking")
# //child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak() 


# 4.2)Multilevel inheritence(one base class and multiple derived class,one derived class inherts another direved class)

# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# class DogChild(Dog):
#     def eat(self):
#         print("eating bread...")
# d=DogChild()
# d.bark()
# d.speak()
# d.eat()


# 4.3)Multiple inheritence(multiple base class and single derived class)

# class Calculation1:
#     def summation(self,a,b):
#         return a+b
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b
# d=Derived()
# print(d.summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))
        

# 4.4)Hierarchical inheritence(single parent class and  multiple derived class)

# class Parent:
#     def func1(self):
#         print("this function is in parent class.")
# class Child1(Parent):
#     def func2(self):
#         print("this function is in child1.")
# class Child2(Parent):
#     def func3(self):
#         print("this function is in child2.")
# d=Child1()
# d.func1()
# d.func2()
# d=Child2()
# d.func1()
# d.func3()

# 4.5)HYBRID INHERITENCE (use morethan one inheritence in a single program)

# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Pet:
#     def show_affection(self):
#         print("Pet shows affection")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barking")
# class DogChild(Dog, Pet):
#     def eat(self):
#         print("Eating bread...")
# d = DogChild()
# d.bark()            
# d.speak()           
# d.eat()             
# d.show_affection()  

# 5)POLYMORPHISM(it is the ability to take morethan one form)

# class Bank:
#     def getroi(self):
#         return 10;
# class SBI(Bank):
#     def getroi(self):
#         return 7;
# class ICICI(Bank):
#     def getroi(self):
#         return 8;
# b1=Bank()
# b2=SBI()
# b3=ICICI()
# print("Bank rate of interset",b1.getroi());
# print("SBI rate of interset",b2.getroi());
# print(" ICICI rate of interset",b3.getroi());

# 6.)ENCAPSULATION(wrapping up of data is called encapsulation)
# 6.1)protected member

# class Base: 
# 	def __init__(self): 	
# 		self._a = 2
# class Derived(Base): 
# 	def __init__(self): 		
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", self._a)  
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", self._a) 
# obj1 = Derived() 
# obj2 = Base() 
# print("Accessing protected member of obj1: ", obj1._a) 
# print("Accessing protected member of obj2: ", obj2._a) 

# 6.2)private member

# class Base: 
#     def __init__(self): 
#         self.a = "Hello"
#         self.__c = "World" 
# class Derived(Base): 
#     def __init__(self):  
#         Base.__init__(self) 
#         print("Calling private member of base class: ") 
#         print(self.__c) 
# obj1 = Base() 
# print(obj1.a) 



# 7.)DATA ABSTACTION()

# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
# dog = Dog()
# cat = Cat()
# print(dog.make_sound())
# print(cat.make_sound())
