values = [1, 2, "krish", 3, 4, "vasu"]

print(values[0])
print(values[2])
print(values[-1])
values.insert(3, "kutty")
print(values)
values[2]= "vasu"
print(values)
print(values[1:4])
values.append("dandanakka")
print(values)
del values[0]
print(values)


listname= ["value1", "value2", "value3"]
print(listname[0])
print(listname[-1])
listname.insert(1, "value4")
print(listname)

listname[1]= "values5"
print(listname)

print(listname[1:3])
listname[3]= "hey"
print(listname)

listname.append(4567)
print(listname)
del listname[0]
print(listname)


