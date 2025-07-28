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

    

     