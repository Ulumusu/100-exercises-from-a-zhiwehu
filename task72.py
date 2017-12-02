import random
l=[]
for x in range(200):
    if x%5==0 and x%7==0 :
        l.append(x)
print(l)        
print (random.choice(l))
