class Form:
    def printData(self):
        print(f"Name is {self.name}")
        print(f"College is {self.college}")

PeeyushApplication = Form() #object created
PeeyushApplication.name = "Peeyush Gaur"
PeeyushApplication.college = "DSCE"
PeeyushApplication.printData()