class A:
    x = 0
    def add(self,a, b):
        return a + b

    def getx(self):
        return self.x 

    def setx(self, newx):
        self.x = newx

class B(A):
    cheese = ""
    x = 0

    def __init__(self, newcheese):
        self.cheese = newcheese

    def getCheese(self):
        return self.cheese

    def setCheese(self, newcheese):
        self.cheese = newcheese
    

# new cheese obj
ayo = B("blue cheese")
print(ayo.getCheese())
ayo.setCheese("green cheese")
print(ayo.getCheese())
print(ayo.getx)
ayo.setx(9)
print(ayo.getx)
