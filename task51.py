class shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class square(shape):
    def __init__(self, l):
        shape.__init__(self)
        self.lenght=l

    def area(self):
        return self.lenght*self.lenght


asquare=square(3)
print (asquare.area())
