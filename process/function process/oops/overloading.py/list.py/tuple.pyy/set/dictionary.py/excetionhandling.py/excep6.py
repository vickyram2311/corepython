#riseexception or error
try:
    pas=input("enter the password")
    con=input("enter the confirm password")
    if pas != con:
        raise annamalaierror
    
    else:
        print("password set sccuess")
except annamalaiarror as an:
    print(an)
finally:
    print("sucessfully login")
    
