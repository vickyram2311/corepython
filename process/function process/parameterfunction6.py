def demo():
    exp=int(input("tell a experience"))
    skil=(input("tell a skill"))
    if exp<=5 and exp>=10 and skil =="python" or skil=="java":
        print("promoted as hr")
    elif exp<=7 and exp>=12 and skil == "darkweb" or skil=="develop":
        print("promoted as manager")
    #return"be an associate"
to=demo()
print(to)
