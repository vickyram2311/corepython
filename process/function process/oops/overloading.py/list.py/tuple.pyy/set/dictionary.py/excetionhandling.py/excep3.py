#value error
try:
    num=int(input("enter the number"))
    print(num)

except ValueError as e:
    print("value error",e)
    print("krish")