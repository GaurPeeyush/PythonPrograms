class Employee:
    company = "Google"
    def getsalary(self):
        print(f"Salary for this  employee working in {self.company} is {self.salary}")
Peeyush = Employee() #Peeyush is given, which will be passed to getsalary by default without showing
Peeyush.salary = 10000
Peeyush.getsalary() #Employee.getsalary(Peeyush)