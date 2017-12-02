l=[]

n=int(input())

def even_num(n):
    for x in range(0, n+1):
        if x%5==0 and x%7==0:
            l.append(str(x))
    return l
    
        
even_num(n)   
print(",".join(l))


