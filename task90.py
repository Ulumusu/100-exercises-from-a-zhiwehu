class Person(object):
    def getGender(self):
        return "unknown"
class male(Person):
    def getGender(self):
        return "male"

class female(Person):
    def getGender(self):
        return "female"

amale=male()
afemale=female()
aPerson=Person()
print (amale.getGender())
print (afemale.getGender())
print(aPerson.getGender())
