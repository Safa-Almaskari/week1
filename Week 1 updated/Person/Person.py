class Person:
    # constructor to create objects
    # initailize instance variables
    def __init__(self,name, age, salary): #default age value
        self.name = name
        self.age = age
        self.salary = salary
    
    def bounce(self):
        b = self.salary * 0.005
        return b
        
    def say_hi(self):
        return f"Welcome {self.name} as Person"
        
        
    #use term of encapsualtion
        #accessor methods:
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
        #settr / mutotur methods 
    def set_name(self,newName):
        self.name =newName
    def set_age(self,newAge):
        self.age = newAge
        
        #printing a string
    def run(self):
        print(self.name, "is runnning")
        
        #returning a string
    def descrip(self):
        return f"Person's name {self.name} is {self.age} years old"
    
    def laugh(self):
        print(self.name, 'say hahaha')
  


        
        
        
        
        
        