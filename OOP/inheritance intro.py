class Employee:
  def _init_(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee(123,"sanju")
e1.showDetails()
# e2 = Programmer("Harry", 4100)
# e2.showDetails()
# e2.showLanguage()