class rectangle(object):
    def __init__(self, height,width):
        self.height=height
        self.width=width

    def pole(self):
        return (self.height)*(self.width)
    
one=rectangle(4,3)

print(one.pole())
