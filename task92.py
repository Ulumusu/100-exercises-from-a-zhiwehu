write=input()
write= write[::-1]
print(write,"\n")
s=[]
s.append(write)
print(s[::-1])

dic={}
for write in write:
    dic[write]=dic.get(write,0)+1

print("\n".join(["%s,%s" % (k,v) for k,v in dic.items()]))    
