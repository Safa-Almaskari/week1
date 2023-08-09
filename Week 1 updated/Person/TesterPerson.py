from Person import Person
from StudentClass import Student
from TeacherClass import Teacher
 
def main():
    Hanaa = Person("Hanaa Al-Zadjali", 23, 2000)
    person2 = Person("Hamza", 25, 5000)
    #print(Hanaa.say_hi())
    #print(person2.say_hi())
    
    std1 = Student("Latifa", 18, 2021)
    std2 = Student("Harith", 21, 2022)
    #std2.run()
    #print(std1.say_hi())
    #print(Student.say_hi(std2))
    #print(std1.descrip())
    
    teach1= Teacher("Dr.Loui", 45, 20100, 2010)
    teach2 = Teacher("Dr.Sara", 35, 2000, 2012)
    #print(teach1.say_hi())
    #print(Teacher.say_hi(teach2))
    #teach1.laugh()
    
    
    
    print(person2.descrip())
    print(Hanaa.get_name())
    
    Hanaa.set_name("Hanaa AbdulWahab Al-Zadjali")
    print(Hanaa.get_name())
    print(Hanaa.descrip())
    Hanaa.run()
    Hanaa.laugh()
    person2.laugh()
    
    print(std1.say_hi())
    print(Student.say_hi(std2))
    std2.run()
    
    print(teach1.say_hi())
    print(Student.say_hi(teach2))
    teach1.laugh()
    
    print(Hanaa.say_hi())
    print(Person.say_hi(person2))
    
    
main()
