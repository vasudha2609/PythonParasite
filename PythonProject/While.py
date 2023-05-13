it = 6

while it>1:
    print(it)
    it = it-1

print("*********************")
#to print first 5 numbers using while loop
i=1
n=5
while i<=n:
    print(i)
    i=i+1
print("*****************")
#to skip a particular number in while using if condition

i = 6
while i>1:
    if i == 3:   #break condition in while loop
        break
    print(i)
    i = i - 1

#to find first five multiples of six
i = 1
while i<=10:
    print("6*", (i), "=", 6*i )
    if i>=5:
        break
    i = i+1
print("*******************")

#multiples of 9 till 15
i = 1
while i<=20:
    print("9*",(i),"=", 9*i)
    if i==15:
        break
    i=i+1

print("*************************************8")

i= 10
while i>1:
    if i==4:
        i=i-1
        continue
    if i==1:
        break
    print(i)
    i = i-1

print("***************")

i=10
while i>1:
    if i==5:
        continue
    print(i)
    i= i - 1





