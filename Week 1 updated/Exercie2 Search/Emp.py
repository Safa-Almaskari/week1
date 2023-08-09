import pandas as pd
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

# binary search 
def binary_search_employees(employee_list, target_empid):
    left, right = 0, len(employee_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if employee_list[mid].emp_id == target_empid:
            return employee_list[mid]
        elif employee_list[mid].emp_id < target_empid:
            left = mid + 1
        else:
            right = mid - 1
    return None

#Excel file
x = 'Employee.xlsx'
df = pd.read_excel(x)
employee_objects = [Employee(row['Name'], row['ID'], row['Salary']) for index, row in df.iterrows()]

# Sorting list 
employee_objects.sort(key=lambda emp: emp.emp_id)

# Searching Employee using binary search
target_employee_id = 1515  #using employee ID in excel sheet
found_employee = binary_search_employees(employee_objects, target_employee_id)
if found_employee:
    print(f"Employee is available: {found_employee.name} and salary is: {found_employee.salary}")
else:
    print("Employee not available:(")