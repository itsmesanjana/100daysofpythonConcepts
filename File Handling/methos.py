# # Readline()
# f=open('myfile.txt','r')
# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break
#Readlines()
# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1}")
#   print(f"Marks of student {i} in English is: {m2}")
#   print(f"Marks of student {i} in SST is: {m3}")

#   print(line)
  #Writelines()
# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

#seek() and tell()
# with  open('file.txt', 'r') as f:
#     print(type(f))
#     #Move to the 10th byte in the file
#     f.seek(10)
#     #Read the next 5 bytes
#     print(f.tell())
#     data=f.read(5)
#     print(data)

#Truncate()
with open('sample.txt','w') as f:
    f.write('Hello World')
    f.truncate(5)
