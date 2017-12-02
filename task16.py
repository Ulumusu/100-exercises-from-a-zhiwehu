#Question 16
#Level 2

#Question:
#Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
#Suppose the following input is supplied to the program:
#1,2,3,4,5,6,7,8,9
#Then, the output should be:
#1,3,5,7,9

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

a=input("wpisz liczby oddzielając przecinkiem:")

number=a.split(",")
print("to są twoje liczby:")
print(number)
my_num=[]
for x in number:
    x=int(x)
    if x%2!=0:
        my_num.append(x)

print("to są liczby nieparzyste:")
print(my_num)

    
