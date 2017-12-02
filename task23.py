#Question 23
#level 1

#Question:
    #Write a method which can calculate square value of number

#Hints:
    #Using the ** operator


def power(number,pw):
    result=int(number)**int(pw)
    return print("Result: %d" %(result))

while True:
    number=input("Number please: ")
    pw=input("Power please: ")
    if not number:
        print("Nothing")
        break
    if not pw:
        print("Nothing mean zero (0)\nResult: 1")
    power(number, pw)    
