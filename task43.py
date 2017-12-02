lista=[1,2,3,4,5,6,7,8,9,10]
lista1=list(filter(lambda x: x%2==0, lista))
print(lista1)


for x in lista:
    if x%2==0:
        print(x)
       
