#Question:
#Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
#D 100
#W 200
#¡­
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be:
#500




#------------------------------------------------------------------------


account=0 #YOUR BANK ACCOUNT

def first(CASH):
    global account
    account=account+CASH
    return account

def second(CASH):
    global account
    if account<=0:
        print("You don't have a money")
    else:
        account=account-CASH
        if account<0:
            print("You don't have a money")
            account=0
    return  account


    
#------------------------------------------------------------------

import datetime
Time = datetime.datetime.now()
print (Time)

print("######################################################################")            
print("Welcome!!! What do you want to do?")
print("######################################################################")            


FIRST_ANSWER=input("DEPOSIT (d)\nWITHDRAWAL (w)\nACCOUNT STATUS (a)\nQUIT (q)\nANSWER: ")

while FIRST_ANSWER!="q":
    if FIRST_ANSWER=="d":
        CASH=int(input("Your cash please: "))
        first(CASH)
        FIRST_ANSWER=input("\n\nDEPOSIT (d)\nWITHDRAWAL (w)\nACCOUNT STATUS (a)\nQUIT (q)\nANSWER: ")
        
    elif FIRST_ANSWER=="w":
        CASH=int(input("Your cash please: "))
        second(CASH)
        FIRST_ANSWER=input("\n\nDEPOSIT (d)\nWITHDRAWAL (w)\nACCOUNT STATUS (a)\nQUIT (q)\nANSWER: ")
        
    elif FIRST_ANSWER=="a":
        print("---------------------")
        print("Your Account: %d" %(account))
        print("---------------------")
        FIRST_ANSWER=input("\n\nDEPOSIT (d)\nWITHDRAWAL (w)\nACCOUNT STATUS (a)\nQUIT (q)\nANSWER: ")
        
    else:
        print("Goodbye")
        break


            
