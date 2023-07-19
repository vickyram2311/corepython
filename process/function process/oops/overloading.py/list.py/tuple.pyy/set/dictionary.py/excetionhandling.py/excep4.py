try:
    li=[10,20,30,40,50]
    print(li[6])
except IndexError as e:
    print("index error",e)