#for loop

obj= [2, 3, 5, 7, 9]
for i in obj:
    print(i)

#print the sum of first five natural numbers

summation= 0
for i in range(1, 6):  # range(i, j) -> i toj-1 #range has round
    summation = summation + i
print("{}{}".format("Total Summation Value is ", summation))

values= range(4)
for i in values:
    print(i)

print("***********************")
values= range(1, 10, 2)
for i in values:
    print(i)



