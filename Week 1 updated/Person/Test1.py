from Person import Person
from Teacher import Teacher
def main():
    p1 = Person('Ahmed', 24, 1500)
    t1 = Person('Dr.Ali', 41, 20000)
    print(p1.descrip())
    print(p1.bonuce())
    print(t1.descrip())
    print(t1.bonuce())

main()