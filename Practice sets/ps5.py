# class MyClass:
#     def __init__ (self,value):
#         self._value=value
#     def show(self):
#         print(f"value is {self._value} ")
#     @property
#     def value(self):
#         return self._value
    
# obj=MyClass (10)
# print(obj._value)
# obj.show()

###snake water gun game###

import random
def check(comp,user):
 if comp==user:
    return 0
 if (comp==0 and user==1):
     return -1
 if (comp==1 and user==2):
     return -1
 if(comp==2 and user==0 ):
     return -1

 return 1

comp=random.randint(0,2)
user=int(input("0 for Snake,1 for water and 2 for Gun:\n"))

score=check(comp,user)

print("You:",user)
print("Computer:",comp)

if(score==0):
    print("It's a tie")
elif(score==-1):
    print("You Lose")
else:
    print("You Won")