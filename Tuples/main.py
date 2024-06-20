tup=(1,5,6,"sanjana")
# tup[0]=90 
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-2])
if 342 in tup :
    print("Yes,342 is in tuple")
else:
    print("No,It's not there..")
    tup2=tup[1:4]
    print(tup2)
