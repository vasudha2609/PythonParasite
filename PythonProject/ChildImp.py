from Oops1 import calculator


class childimp(calculator):
    num2= 200

    def __init__(self):
        calculator.__init__(self, 2, 3)
        self.sub_integers(4, 5)

    def get_complete_data(self):

        return self.num2+ self.num+ self.summation()


obj = childimp()
print(obj.get_complete_data())


