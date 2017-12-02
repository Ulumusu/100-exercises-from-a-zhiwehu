num=[5,6,77,45,22,12,24]
for x in num:
    if x%2==0:
        num.remove(x)

print(num)        



#other
num2=[5,6,77,45,22,12,24]
num2=[x for x in num if x%2!=0]
print(num2)
