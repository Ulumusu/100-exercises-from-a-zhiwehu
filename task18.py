#Question:
#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345
#Then, the output of the program should be:
#ABd1234@1

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input



import re # check criteria
def check_a_z(user_password):
    if not re.search("[a-z]",user_password):
        print("wrong at least 1 letter between [a-z]")
    elif not re.search("[0-9]",user_password):
        print("wrong at least 1 letter between [0-9]")
    elif not re.search("[A-Z]",user_password):
        print("wrong at least 1 letter between [A-Z]")
    elif not re.search("[$#@]",user_password):
        print("wrong at least 1 letter between [$#@]")
    elif re.search("\s",user_password):
        print("wrong")
    else:
        pass
        print(user_password)
    

def check_len(user_password): #check len password
        if len(user_password)>6 and len(user_password)<12:
            check_a_z(user_password)
        else:
            if len(user_password)<6:
                print("To short")
            elif len(user_password)>12:
                print("To long")
             


#------------------------------------


#you give login and password
user_login=input("login: ")
print("Your Login is: %s" % (user_login))
user_password=input("Password: ")
check_len(user_password)



