num=[12,24,35,70,88,120,155]
num=[x for (i,x) in enumerate(num) if i not in (0,4,5)]
print(num)



num2=[12,24,35,70,88,120,155]
num2=[x for (x,i) in enumerate(num) if i not in (12,35,88)]
print(num2)
