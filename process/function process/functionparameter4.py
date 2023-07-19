balance=[250000,3000,45000,5500]

def debit(money=0,pos=0):
    if money<=balance[pos]:
        balance[pos]-=money
        print(money,"debited")
        return balance[pos]
    else:print("cant debited")

hai=debit(2500,3)
print(hai)


