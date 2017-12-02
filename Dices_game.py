# this is a dice game. I GIVE ALL IN  ONE FUNCTION IF YOU HAVE

def game():
    print("Welcome in my game.\nFirst choose number. How many dice do you have? ")

    # YOU
    number_of_dice = int(input("Answer: "))
    print("")
    number_of_dice += 1
    if number_of_dice:
        dice = [1, 2, 3, 4, 5, 6]
        your_sum = 0
        for x in range(1, number_of_dice):
            import random
            a = (random.choice(dice))
            your_sum += a
            print("Your dice: %d" % x)
            print("Your number:%d" % (a))
            print("------------------")

    # COMPUTER
    print("YOUR SUM:%d\n\nNow this is turn on the computer\n" % (your_sum))

    computer_sum = 0
    for x in range(1, number_of_dice):
        import random
        b = (random.choice(dice))
        computer_sum += b
        print("Computer dice: %d" % x)
        print("Computer number:%d" % (b))
        print("------------------")

    print("COMPUTER SUM:%d" % (computer_sum))
    print("\n=============================")

    # RESULT
    print("You:%d" % (your_sum))
    print("Computer:%d" % (computer_sum))
    if your_sum > computer_sum:
        print("RESULT: Congratulations you win!!!")

    elif your_sum == computer_sum:
        print("RESULT: Nobody won")
    else:
        print("RESULT: You loose")

    # PLAY AGAIN IF YOU WANT
    into2 = input("\nDo you want play again? (y or n)")
    while into2 != "n":
        if into2 == "y":
            game()
        elif into2 == "n":
            print("shame")
            break
        else:
            break
    return


# START
into = input("Do you want play? (y or n)")

if into == "y":
    game()
elif into == "n":
    print("shame")
    import sys

    sys.exit()