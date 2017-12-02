l=[]
n=int(input())

def even_num(n):
    for x in range(0, n+1):
        if x%2==0:
            l.append(str(x))
    return l
        
even_num(n)   
print(",".join(l))



#another



def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print (",".join(values))
