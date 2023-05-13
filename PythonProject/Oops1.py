class calculator:
    num=100 #class variables

    def __init__(self, a, b):
        self.number1 = a  #instance variables
        self.number2 = b  #instance variables

        print(f"Add integers ={self.number1+self.number2}")

    def sub_integers(self, c, d):
        self.number3 = c #instance variables
        self.number4 = d #instance variables
        print(f"subtract integers= {self.number3-self.number4}")

    def summation(self):
        totalValue =self.number1 + self.number2 + (self.number3 - self.number4) + calculator.num
        print(f"total sum ={totalValue}")
        return totalValue



obj= calculator(23,32)
obj.sub_integers(12,6)
obj.summation()

# Points to Remember:
# Class variables can be accessed by using both Self and Classnames
# Instance Variables can only be accessed through self only.
# self belongs to object of Class.
