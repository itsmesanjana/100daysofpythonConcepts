#Tupels are immutable....
# countries=("Spain","Itlay","India","England","Germany")
# temp=list(countries)
# temp.append("Russia") #Add Item
# temp.pop(3)  #remove item
# temp[2]="Finland" # change item
# countries=tuple(temp)
# print(countries)
#####Concatination######
# countries=("Pakistan","Afghanistan","Bangladesh","Shrilanka")
# countries2=("Vietnam","India","China")
# southEastAsia=countries+countries2
# print(southEastAsia)
###Count&Index####
tup1=(0,1,2,3,5,5,4,1,4,5,2,1)
# res=tup1.count(1)
# res=tup1.index(3)
res=tup1.index(4,4,8) #Here 1st value indicates the no which u want the index to access and 2nd,3rd is used for slicing
# print("Count of 1 in tup1 is :",res)
print("Index of 5 in tup1 is :",res)
