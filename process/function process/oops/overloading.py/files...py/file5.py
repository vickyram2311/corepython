#read binary

from pickle import *
name=open("mydata.txt","rb")
while True:
    try:
        studentdata=load(name)
        print(studentdata)
    except EOFError as e:
        break



