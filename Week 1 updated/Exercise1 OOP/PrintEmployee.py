if __name__ == "__main__":
    employees = [
        Employee("ADAMS", "E7876", 50000, "ACCOUNTING"),
        Employee("JONES", "E7499", 45000, "RESEARCH"),
        Employee("MARTIN", "E7900", 50000, "SALES"),
        Employee("SMITH", "E7698", 55000, "OPERATIONS")
    ]

    for employee in employees:
        print("\nEmployee Details:")
        employee.print_employee_details()

        new_department = input("\nEnter new department: ")
        employee.emp_assign_department(new_department)

        hours_worked = int(input("Enter hours worked: "))
        total_salary = employee.calculate_emp_salary(hours_worked)
        print("Total Salary:", total_salary)