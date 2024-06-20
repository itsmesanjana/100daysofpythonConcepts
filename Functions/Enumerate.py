marks=[12,56,32,98,12,45,1,4]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#      print("Harry,Awsome!")
#     index+=1
index=0
# for mark,index in enumerate(marks,start=1):#It displays the total indeces of the marks 
for index,mark in enumerate(marks,start=1):#It displays the total marks at particular index... 
    print(mark)
    if(index==3):
     print("Harry,Awsome!")
    # index+=1