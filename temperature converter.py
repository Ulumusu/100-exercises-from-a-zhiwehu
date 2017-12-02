#Temperature converter

import sys

def return_to_menu():
     dec2=input("(1) You return to main menu\n(2) You finish\n")
     if dec2=="1":
            main_menu()
     elif dec2=="2":
            sys.exit()
     else:
            sys.exit()
        

def c_to_f():
    print("\n°C°C°C°C°C =======> F°F°F°F°F")
    give=int(input("Give me the number: "))
    result=give*(9/5)+32
    print("Result: %d°F" % (result))
    print("°C°C°C°C°C =======> °F°F°F°F°F")
    again=input("Do you want check again?\n(1) Yes\n(2) No\n")
    if again=="1":
        c_to_f()
    else:    
        return_to_menu()

    
def f_to_c():
    print("\n°F°F°F°F°F =======> °C°C°C°C°C")
    give=int(input("Give me the number: "))
    result=(give-32)/1.8000
    print("Result: %d°C" % (result))
    print("°F°F°F°F°F =======> °C°C°C°C°C")
    again=input("Do you want check again?\n(1) Yes\n(2) No\n")
    if again=="1":
        f_to_c()
    else:    
        return_to_menu()
    

def c_to_k():
    print("\n°C°C°C°C°C =======> K K K K K ")
    give=int(input("Give me the number: "))
    result=give+273.15
    print("Result: %dK" % (result))
    print("°C°C°C°C°C =======> K K K K K ")
    again=input("Do you want check again?\n(1) Yes\n(2) No\n")
    if again=="1":
        c_to_k()
    else:    
        return_to_menu()
        
def f_to_k():
    print("\n°F°F°F°F°F =======> K K K K K ")
    give=int(input("Give me the number: "))
    result=(give+459.67)*(5/9)
    print("Result: %dK" % (result))
    print("°F°F°F°F°F =======> K K K K K ")
    again=input("Do you want check again?\n(1) Yes\n(2) No\n")
    if again=="1":
        f_to_k()
    else:    
        return_to_menu()

def k_to_c():
    print("\nK K K K K =======> °C°C°C°C°C ")
    give=int(input("Give me the number: "))
    result=give-273.15
    print("Result: %d°C" % (result))
    print("K K K K K =======> °C°C°C°C°C ")
    again=input("Do you want check again?\n(1) Yes\n(2) No\n")
    if again=="1":
        k_to_c()
    else:    
        return_to_menu()

def k_to_f():
    print("\nK K K K K =======> °F°F°F°F°F ")
    give=int(input("Give me the number: "))
    result=(give*(9/5))-459.67
    print("Result: %d°F" % (result))
    print("K K K K K =======> °F°F°F°F°F ")
    again=input("Do you want check again?\n(1) Yes\n(2) No\n")
    if again=="1":
        k_to_f()
    else:    
        return_to_menu()
    

def select_option(decision):
        if decision=="1":
            c_to_f()
        elif decision=="2":
            f_to_c()
        elif decision=="3":
            c_to_k()
        elif decision=="4":
            f_to_k()
        elif decision=="5":
            k_to_c()
        elif decision=="6":
            k_to_f()
        elif decision=="7":
            print("Goodbye")
            sys.exit()
        else:
            main_menu()

def main_menu():
    print("Welcome to temperature converter")
    decision=input("Choose option:\n(1) °C to °F\n(2) °F to °C\n(3) °C to K\n(4) °F to K\n(5) K to °C\n(6) K to °F\n(7) Quit\n(choose number) ")
    select_option(decision)

main_menu()
