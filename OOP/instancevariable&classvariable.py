class Employee:
    companyName="Apple"#Class variables
    noOfEmployee=0#This too
    def __init__(self,name):
        self.name=name #Instance variables
        self.raise_amount=0.02
        Employee.noOfEmployee+=1
    def showDetails(self):
        print( f"The Name of Employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")
    
emp1=Employee("Harry")
emp1.raise_amount=0.3
emp1.companyName="Apple India"
emp1.showDetails()
Employee.companyName="Google"
print(Employee.companyName)

emp2=Employee("Rohan")
emp2.companyName="nestle"
emp2.showDetails()