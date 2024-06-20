# import time
# name=input("Enter Your Name:")
# currtime=time.strftime('%H:%M:%S')
# Currtime=int(time.strftime('%H'))
# c=name.capitalize()
# if(4<=Currtime<12):
#     print("Good Morning",c,'its',currtime)
# elif(12<=Currtime<17):
#     print("Good Afternoon",c,'its',currtime)
# elif(17<=Currtime<21):
#     print("Good Evening",c,'its',currtime)
# else:
#     print("Good Night",c,'its',currtime)
    
    ###Harry Method###
import time
t=time.strftime("%H:%M:%S")
hour=int(time.strftime("%H"))
hour=int(input("Enter hour:"))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning,sir!")
elif(hour>=12 and hour<17):
 print("Good Afternoon,sir!")
elif(hour>=17 and hour<24):
  print("Good Night,sir!")

            


