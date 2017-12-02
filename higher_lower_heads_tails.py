#Higher/lower | Heads/tails

import random  #import becasuse it's required
import sys
     

def higher_lower(): #first game
    n=int(input("first give me the number (max number in game, your border): "))
    num1=(random.randint(0,n))
    try1=1
    print(try1)
    shoot_number=int(input("SHOOT: "))
    while shoot_number!=num1 or try1!=10:
        if shoot_number==num1:
            print("YOU WIN")
            res=input("Do you want play again or go to main  menu\n1 is again\n2 is main menu\n")
            if res=="1":
                higher_lower()
            else:
                main_menu()
        elif shoot_number>num1:
            print("LOWER")
            try1+=1
            print(try1)
            shoot_number=int(input("SHOOT AGAIN: "))
        elif shoot_number<num1:
            print("HIGHER")
            try1+=1
            print(try1)
            shoot_number=int(input("SHOOT AGAIN: "))
        if try1==10:
            print("YOU LOOSE")
            res=input("Do you want play again or go to main  menu\n1 is again\n2 is main menu\n")
            if res=="1":
                higher_lower()
            else:
                main_menu()

def heads_tails(): #second game
    player_score=0
    computer_score=0
    while player_score!=10 or com_score!=10:
        choose=["heads","tails"]
        one=random.choice(choose)
        your_choose=input("heads or tails??\n")
        if one==your_choose:
            player_score+=1
            print("TRUE YOUR SCORE IS %d"% (player_score))
        else:
            computer_score+=1
            print("FALSE COMPUTER SCORE SCORE  %d"% (computer_score))
        if player_score==10:
            print("YOU WIN")
            res=input("Do you want play again or go to main  menu\n1 is again\n2 is main menu\n")
            if res=="1":
                heads_tails()
            else:
                main_menu()
        elif computer_score==10:
            print("YOU LOOSE")
            res=input("Do you want play again or go to main  menu\n1 is again\n2 is main menu\n")
            if res=="1":
                heads_tails
            else:
                main_menu()
    


def main_menu():
    print("======================================")
    player_choice=input("Welcome to the program\n Please choose the game\n(1) if you want play Higher and lower\n(2) if you want play Heads/tails\n(3) if you want quit\n")
    if player_choice=="1":
        higher_lower()
    elif player_choice=="2":
        heads_tails()
    elif player_choice=="3":
        print("Goodbye")
        sys.exit()
    else:
        sys.exit()



        
main_menu()
        
    

