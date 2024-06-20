#Class is a Blueprint or template used to create an object.
class Person:
    name="Sanjana"
    occupation="Student"
    networth=0
    def info(self):
      print(f"{self.name} is a {self.occupation}")
#wo object jiske liye method call kiya ja raha hai...(It iis the reference to the current instance of the class)
a=Person()
b=Person()
c=Person()
a.name="Shri"
a.occupation="ML engineer"

b.name="Nitika"
b.occupation="HR"


# print(a.name,a.occupation)
a.info()
b.info()
c.info()
