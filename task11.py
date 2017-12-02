

number=[x for x in input().split(",")]

lista=[]

for x in number:
  number2=int(x, 2)
  if number2%5==0:
    lista.append(x)
    print("this is normal form: " + str(number2))
    print("this is binary form: "+ bin(number2))
    print(",".join(lista))