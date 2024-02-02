class Employee:
    def __init__(self,emp_ID, emp_name, position,salary):
        self.emp_ID = emp_ID
        self.emp_name = emp_name
        self.position = position
        self.salary = salary
    def display_details(self):    
        return f"Employee ID: {self.emp_ID}\nName: {self.emp_name}\nPosition: {self.position}\nSalary: {self.salary}"
    def update_salary(self,new_salary):
        self.salary = new_salary
        return f"the updated salary is {self.salary}"
    
employee1 = Employee("Ravi", 101, "Software Engineer", 80000)
employee2 = Employee("Saket", 102, "Data Scientist", 90000)

print(employee1.display_details())
print(employee2.display_details())

# updating salary 
new_salary = 340000
update_message = employee1.update_salary(new_salary)
print("\n", update_message)
