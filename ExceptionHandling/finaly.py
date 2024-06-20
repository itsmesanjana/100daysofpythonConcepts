# def func1():
    
# try:
#        l=[1,5,6,7] 
#     i=int(input("Enter the index:"))
#     print(l[i])
#     return 1
# except:
#     print("Some error ocured")
#     return 0
# # finally:
#     print("I am always executed") #It doesn't works in the condition of function case if error produces in above lines of code
    
# x=func1()
# print(x)

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)
