# # def  cube(x):
# #     return x*x*x 
# # print(cube(2))

# l=[1,2,4,6,4,3]
# # newl=[]
# # for item in l:
# #     newl.append(cube(item))
# # print(newl)

# #Map() function

# newl=list(map(lambda x: x*x*x,l)) #map(function,listname/iterable)
# print(newl)

# #Filter() functions
# def filter_function(x):
#     return x>3
# newl=list(filter(filter_function,l))
# print(newl)

# ###It's possible that fuunction can take the function as an argument###


from functools import reduce
no=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,no)
print(sum)
