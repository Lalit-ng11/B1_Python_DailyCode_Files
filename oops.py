'''
Rules to define a Class:- 
1.class keyword ,
2.classname should start with Capital Letter.
3.it should contain constructor method (__init__)
'''
# class Student:
#     def __init__(self,id,name,course):
#         self.id=id #instance variable/ Data Members(Variables)
#         self.name=name 
#         self.course=course
        
#     def details(self): #Member Functions
#         return f"student id is {self.id}.Name is {self.name} and course is {self.course}"

# s1=Student(101,"Rahul","PFS")
# # print(s1)
# '''<__main__.Student object at 0x000001CB440E6A50>'''
# print(s1.details())

# #Data Members(Variables) and Member Functions. 
'''
oops concepts:- 
class,objects,
Inheritance:- properties of  Base /Parent class is inherited/accessed by Child class. is a relationship
Types of Inheritance=>
1.Single Inheritance[p-> c],
2.Multiple Inheritance[p-> c,<- p] 
3.Multilevel Inheritance[GP->P->C]
4.Hirarchical Inheritance[P->c1
                           ->c2]
5.Hybrid Inheritance[combination of 2 or many types of inheritance],


Encapsulation,
Polymorphism,
Abstaction
'''
#1.Single Inheritance[p-> c]
class App:
    def __init__(self,name,version,company):
        self.name=name  #Instance Variable
        self.version=version
        self.company=company
        
    def app_info(self):
        return f"App name is {self.name}.it's version is {self.version}.company is {self.company}"
    
class Insta(App): 
    def __init__(self, name, version, company,feature):
        super().__init__(name, version, company)
        self.feature=feature
        
    def all_info(self):
        return f"App name is {self.name}.it's version is {self.version}.company is {self.company} and it is having {self.feature} feature."
    
info=Insta("Insta",142,"Meta","Reels")
print(info.all_info())
'''
o/p = 
App name is Insta.it's version is 142.company is Meta and it is having Reels feature.
'''
    