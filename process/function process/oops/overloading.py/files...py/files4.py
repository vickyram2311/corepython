#write binary

from pickle import *
name=open("mydata.txt","wb")

studentdata=[501,"vicky","avs","clddge"]

collegename={"name=ram","college=avs","rollno=234456"}

myfrndname=("magi","raja")

dump=(studentdata,name)
dump=(collegename,name)
dump=(myfrndname,name)
name.close()