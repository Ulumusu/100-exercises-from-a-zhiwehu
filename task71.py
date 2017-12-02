import random
l=[]
for x in range(11):
    if x%2==0:
        l.append(x)
print (random.choice(l))


#krócej

print (random.choice([i for i in range(11) if i%2==0]))
