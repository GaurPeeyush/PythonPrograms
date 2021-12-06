class Employee:
    company = "Google" # Class Attribute
    salary = 100 
Peeyush = Employee()
Nidhi = Employee()
Peeyush.salary = 1000 #Instance Attribute
print(Peeyush.salary)
print(Nidhi.salary)
print(Peeyush.company)
print(Nidhi.company)
Employee.company = "YouTube" #Instance Attribute will be taken
print(Peeyush.company)
print(Nidhi.company)