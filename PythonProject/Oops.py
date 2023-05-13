class calculator:
    num = 100

    def getdata(self):
        print("I'm now executing a method in class")

    def __init__(self):
            print(" This will be printed automatically")

    def Summation(self,a,b):
        sum=a+b
        print(sum+calculator.num)
        return sum+calculator.num

obj= calculator()
obj.getdata()
print(obj.num)
print(obj.Summation(2,3))

print("**************************************")
class parrot:
    name = ""
    color= ""

    def breed(self):
        print("The breed of the parrot is cocktail")


parrot1 = parrot()
parrot1.name= "oreo"
parrot1.color= "yellow"


parrot2= parrot()
parrot2.name= "tintin"
parrot2.color="blue"

print(f"{parrot1.name} is {parrot1.color} in color")
print(f"{parrot2.name} is {parrot2.color} in color")
# f is formatted string literal, These strings may contain replacement fields.

#"{}{}".format("this is ", 5)


