#remove tuple list covert
a=("sam","sathish","anu","pk","raja")
b=list(a)
b.remove("pk")
a=tuple(b)
print(a)
