#1
# def square(num):
#     return num**2
# object_=square(6)
# print("The square of the given number is:",object_)

#2
# def square(num):
#      print( num**2)
# square(6)


#3
# def a_function(string):
#     return len(string)
# print(a_function("Functions"))
# print(a_function("Python"))


#4
#types of functions
#4.1)with argument with return type
#def square(num):
#     return num*num
# result=square(5)
# print("Square:",result)


#4.2)with argument without return type
# def greet(name):
#     print("Hello",name+"!")
# greet("Anu")

#4.3)without argument with return type
# def get_message():
#     return "Welcome to python programming!"
# msg=get_message()
# print(msg)

#4.4)without argument with return type
# def print_numbers():
#     for i in range(1,6):
#         print(i)
# print_numbers()

# 5.Function Argument
#5.1)Default Argument
# def function(n1,n2=20):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("passing only one argument")
# function(30)

#5.2)Keyword Argument

# def function(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("without using keyword")
# function(n2=50,n1=20)

#6.)
# def display(v):
#     print(v)
    
    
# def addition(a,b):
#     ans=a+b
#     display(f"sum of {a} and {b} is {ans}")
# def substraction(a,b):
#     ans=a-b
#     display(f"substarction of {a} and {b} is {ans}")

# def multtiplication(a,b):
#     ans=a*b
#     display(f"multtiplication of {a} and {b} is {ans}")
# def division(a,b):
#     ans=a/b
#     display(f"division of {a} and {b} is {ans}")

# while True:
#     print("1 . ADDITION")
#     print("2 . substraction")
#     print("3 . multtiplication")
#     print("4 . division")
#     print("5.exit")
#     choice =int(input("enter your choice :"))
#     if (choice == 1):
#         a=int(input("enter a number"))
#         b=int(input("enter the second num"))
#         addition(a,b)
        
#     elif(choice == 2):
#         a=int(input("enter a num"))
#         b=int(input("enter second num"))
#         substraction(a,b)
#     elif(choice == 3):
#         a=int(input("enter a num"))
#         b=int(input("enter second num"))
#         multtiplication(a,b)
#     elif(choice == 4):
#         a=int(input("enter a num"))
#         b=int(input("enter second num"))
#         if(b!=0):
#            division(a,b)
#         else:
#             print("undefined")
#     elif choice==5:
#         print("exiting ......")
#         break


#7.)
# def is_even(num):
#     if num%2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# a=int(input("enter the num"))
# is_even(a)


#######factorialc

# def factorial(num):
#     fact=1
#     for k in range(1,num+1):
#         fact=fact*k
#     print("factorial of the number is",fact)
# n=int(input("enetr your num"))
# factorial(n)


##leap year

# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(year,"is leap year")
#     else:
#         print(year,"is not leap year")
# a=int(input("enter a year"))
# leap_year(a)
        


# def display(name,age):
#     print(f"hello my name is {name} iam {age} years old")
# display("archana",21)



# def display(**a):
#     print(f"hi {a['name']} welome to {a['course']} course")
    
# display(name="archana",course="python")

#8.)Global variable
# a=10
# def fun():
#     global a
#     b=a+25
#     print(b)
# fun()
# def sample():
#     global a
#     c=a-5
#     print(c)
# sample()


#9.)recursion

# def fact(num):
#     if num==1:
#         return num  
#     else:
#         return num*fact(num-1)
# print(fact(5))

#10.)Fibinocci series
# first,second=0,1
# print(first,second,end="")
# for j in range(8):
#     third=first+second
#     print(third,end="")
#     first,second=second,third


#11.)lambda (also called anonymous function)
#lambda_=lambda arg1,arg2:arg1+arg2



#11.)built  in function of a class(get attribute,set attribute,has attribute,delete attribute)

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("John",101,22)
# print(getattr(s,'name'))
# setattr(s,"aeg",23)
# print(getattr(s,'age'))
# print(hasattr(s,"id"))
# delattr(s,'age')
# print(s.age)//to add this print statement the output has error,avoid this statement output has no error

#12.) INHERITENCE
# 12.1)single inheritence(one base class and one derived class)
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


# 12.2)Multilevel inheritence(one base class and multiple derived class)

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


# 12.3)Multiple inheritence(multiple base class and single derived class)

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
        

# 12.4)Hierarchical inheritence(single parent class and  multiple derived class)

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

# 13)POLYMORPHISM(it is the ability to take morethan one form)

