#Question 13
#Level 2

#Question:
#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.




def number(main_sentence):
    d={"digits":0,"letters":0}
    for word in main_sentence:
        if word.isdigit():
            d["digits"]+=1
        else:
           if word.isalpha():
               d["letters"]+=1
    return d
sentence=input("wpisz coś: ")

a=number(sentence)
print(a)

    



