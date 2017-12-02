aist=[]
list=[]
while True:
    s=input()
    if s:
        aist.append(s)
        list.append(s.upper())
    else:
        break


print(', '.join(aist))
print(', '.join(list))