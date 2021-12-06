# Special function to initialise object attributes
class Employee:
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print(f"Employee {self.name} has been created")
        print(self.name)
        print(self.salary)
        print(self.subunit)
Peeyush = Employee("Peeyush", 10000, "Google")# will pass __init__ function by default without even callung it
