# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.
class uppertext():
    def __init__(self):
        self.something = ""

    def getString(self):
        self.something=input()


    def printString(self):
        print(self.something.upper())




x=uppertext()
x.getString()
x.printString()