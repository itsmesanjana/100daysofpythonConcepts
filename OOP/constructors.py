class Person:
   
    #Default parameter involves only self paramenter.
    # def __init__(self):
    #Parameterizied Constructor which iinvolves multiple parameters
    def __init__(self,n,o): 
     print("Hey I am an Engineer")
     self.name=n
     self.occupation=o
    def info(self):
     print(f"{self.name} is a {self.occupation}")
     
a=Person("Harry Potter","Great Artist")
b=Person("Harmineo Granger","Female Lead")
# c=Person(1,2,3) #Here we need to pass only 2 arguments bcz the self itself passes an  default arguments 
a.info()
b.info()

#The main purpose of the constructor is to initialize the object(values) of class.
#It is automatically called when object is created 
#Always returns none 