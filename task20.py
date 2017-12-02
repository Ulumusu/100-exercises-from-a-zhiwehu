box_with_number=[]

number=int(input("wpisz liczbę: "))
for x in range(0,number):
    if x%7==0:
        box_with_number.append(x)
            

print("Te liczby to: \n%s" % box_with_number)
