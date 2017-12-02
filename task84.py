num=[12,24,35,70,88,120,155]
num=[x for (i,x) in enumerate(num) if i%2!=0]

print(num)    


#other
num2=[1,2,3,4,5,6,7,8,9,10]
num2=[x for (i,x) in enumerate(num2) if i%2==0]
num3=[x for (i,x) in enumerate(num2) if i%2!=0]
print(num2)
print(num3)
