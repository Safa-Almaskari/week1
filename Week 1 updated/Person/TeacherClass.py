from Person import Person
class Teacher(Person):
    
    def __init__(self, tname, tage, salary, year): 
        super().__init__(tname, tage, salary)
        self.exper_year = year
        
    def bounce(self):
        b = super().bounce() * 2
        return b
        
    def say_hi(self):
        print(super().say_hi())
        return f"Hello {self.name} as teacher"