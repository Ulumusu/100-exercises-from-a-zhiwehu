def number():
    d=dict()
    for x in range(1,21):
        d[x]=x**2
    for (x,y) in d.items() :
        print(y)

print(number())    
