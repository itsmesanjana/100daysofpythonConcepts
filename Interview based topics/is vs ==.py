#Is compares the exact location of memory(identity of two objects) and == coompares the values

# a=[1,2,43]
# b=[1,2,43]
#It gives true for those data types which are immutable 
a=(1,2)
b=(1,2)
a=2
b=2
#As both variables have same value for now so python points the no at specific one address.So that to reduce the wastage of the memory
print(a is b) #Exact location of object in memory
print(a == b) #value