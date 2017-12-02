class Circle(object):
    def __init__(self, r):
        self.rad=r

    def r2xpi(self):
        return (self.rad**2)*(3.14)
    
one=Circle(4)

print(one.r2xpi())

    
