class Employee:
    company = "Google"
    def getsalary(self):
        print(f"Salary for this  employee working in {self.company} is {self.salary}")
    @staticmethod # Used to avoid passing self parameter in any function, where it's not needed  
    def greet():
        print("Hello, Good Morning!")
Peeyush = Employee() #Peeyush is given, which will be passed to getsalary by default without showing
Peeyush.salary = 10000
Peeyush.getsalary() #Employee.getsalary(Peeyush)
Peeyush.greet()