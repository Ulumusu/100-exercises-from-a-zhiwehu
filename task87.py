num=[12,24,35,24,88,120,155]
for x in num:
    if x==24:
        num.remove(x)
        
print(num)


#other
num2=[12,24,35,88,34,88,24,88,120,155]
num2=[x for x in num2 if x!=24 and x!=88]
print(num2)
