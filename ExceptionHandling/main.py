# a=input("ENter the number:")
# print("Multiplication table of {a} is :")
# try:
#  for i in range(1,11):
#     print(f"{int(a)}X{i}={int(a)*i}")
# except:
#     print("Invalid input")
# # except Exception as e:
# #  print(e)
# print("some lineas of code")
# print("End of program")
try:
    num=int(input("Enter an integer:"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Value error") 

except IndexError:
    print("IndexError")