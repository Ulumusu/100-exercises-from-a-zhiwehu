dic={}
write=input()
for write in write:
    dic[write]=dic.get(write, 0)+1

print("\n".join(["%s,%s" % (k,v) for k, v in dic.items()]))    
