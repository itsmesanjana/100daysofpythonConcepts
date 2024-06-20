# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)
# def isGreater(a,b):
#  if(a>b):
#   print("First is greater than Second")
#  else:
#   print("Second is greater than first")
# def isLesser(a,b):
#   pass    
# # We can write function later without getting any error......
# a=9
# b=8
# # if(a>b):
# #  print("First is greater than Second")
# # else:
# #   print("Second is greater than first")
# # Instedaing writing this we can use this..
# isGreater(a,b)
# # gmean=(a*b)/(a+b)
# # print(gmean) Instedaing writing this we can use this...
# calculateGmean(a,b)
# c=8
# d=71
# # if(c>d):
# #  print("First is greater than Second")
# # else:
# #   print("Second is greater than first")
# isGreater(c,d)
# # gmean2=(c*d)/(c+d)
# # print(gmean2)
# calculateGmean(c,d)


def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        return sum/len(numbers)
    c=average(5,6,7,1)
    print(c)
      