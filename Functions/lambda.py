# def double(x):
#     return x*2
def appl(fx,value):
    return 6+ fx(value)
double=lambda x:x*2 #lambda argument: experasion
cube=lambda x:x*x*x
avg=lambda x,y,z:(x+z+y)/3
print(avg(5,3,10))
print(double(5))
print(cube(5))
print(appl(cube,2))#2^3 is 8 and plus value is equal to the 14