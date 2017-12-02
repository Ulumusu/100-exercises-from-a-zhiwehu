tuple1=(1,2,3,4,5,6,7,8,9,10)
even=list()
for x in tuple1:
    if x%2==0:
        even.append(x)

print(even[:2])
print(even[2:])
print(even) 
