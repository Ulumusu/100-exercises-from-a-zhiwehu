lista=list()
for x in range(1,21):
    lista.append(x)
    lista1=list(filter(lambda x: x%2==0, lista))

    
print(lista1)



even=list(filter(lambda x: x%2==0, range(1,21)))
print(even)


       
