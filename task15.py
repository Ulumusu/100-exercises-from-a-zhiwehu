#Question 15
#Level 2

#Question:
#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.



def task15(a):
    a=int("%s" %(a))
    b=int("%s%s" %(a,a))
    c=int("%s%s%s" %(a,a,a))
    d=int("%s%s%s%s" %(a,a,a,a))

    e=a+b+c+d
    return e


pierwsze=input("t/n: ")
if pierwsze=="t":
    a=input("wpisz: ")
    beniz=task15(a)
    print(beniz)
else:
    import sys
    sys.exit()
    
