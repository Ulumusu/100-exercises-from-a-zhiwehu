class employee():

    raise_amount=1.05
    num=0
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first+ "." +last+"@company.com"

        employee.num+=1

        
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1=employee("corry", "shchafer", 5000)
emp_2=employee("test", "user", 6000)



print(employee.num)

