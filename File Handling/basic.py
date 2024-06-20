# Reading file
# f= open('myfile2.txt','rb')
# print(f)
# text=f.read()
# print(text)
# f.close()


# Writing file
# f=open('myfile.txt','a')
# f.write('Hello World\n')
# f.close()

with open('myfile.txt','a') as f:
    f.write('Hello World\n')