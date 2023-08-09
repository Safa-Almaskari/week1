from Person import Person
#student inhertitante from person 
class Student(Person):
    #constructor
    def __init__(self, sname, sage, year): 
        super().__init__(sname, sage, year)
        self.academic_year = year
        
    #def say_hi(self):
        #return f"Hi {self.name} as student"