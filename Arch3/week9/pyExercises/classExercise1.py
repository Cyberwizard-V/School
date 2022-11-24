class myClass:
    x = 10


x = myClass()
print(x.x)

class Fruits:
    def __init__(self, fruitType):
        self.fruitType = fruitType



myApple = Fruits("Apple")
print(myApple.fruitType)