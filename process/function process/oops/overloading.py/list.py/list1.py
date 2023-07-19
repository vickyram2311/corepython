#demonstration of list
prop=['annamalai',5.5,70,'M']
print(prop)

#adding the new elements in end if list
prop.append('software developer')
print(len(prop))
print(prop)

#adding new element in list
prop.insert(4,15.5)
print(prop)

#replace the data in respective position
prop[5]='team leader'
print(prop)

#adding values in list
monthly=[7000,13000,2000,23000,4000]
print(min(monthly))

#sum of the list(add)
print(sum(monthly))

#remove and pop the list operation
monthly.remove(7000)
print(monthly)
print(monthly.pop())
print(monthly.pop(1))
print(monthly)
print(monthly.reverse())
print(monthly)