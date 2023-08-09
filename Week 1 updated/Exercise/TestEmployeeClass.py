from EmployeeClass import EmployeeClass

def main():
    
    Adams = EmployeeClass("Adams", "E7876", 50000, "Accounting")
    Jonas = EmployeeClass("Jonas", "E7499", 45000, "Reasearch")
    Martin = EmployeeClass("Martin", "E7900", 50000, "Sales")
    Smith = EmployeeClass("Smith", "E7698", 50000, "Operations")
    
    print(Adams.descrip())
    print(Jonas.descrip())
    print(Martin.descrip())
    print(Smith.descrip())
    
main()