# This is number Guessing Game
print("")
print(".................... Number Guessing Game ....................")
print("")
print("")
print("........... Guess the right number to win the Game ...........")
print("")
print("")
print("Hint!  Guess number b/w  [ 1-50 ]")
print("")
print("")
guessnum = 13
chance = 5
i = 1
print("You have total chance :  ", chance)
print("")
while i <= 5:
    if i == 1:
        num = int(input("Guess the number : "))
        print("")
    else:
        num = int(input("Guess the number again : "))
        print("")

    if num == guessnum:
        print("")
        print("")
        print("===============================>>>>>- YOU WIN -<<<<<===============================")
        print("")

        print("  ==         ==    ========    ====      ==    ====      ==    =======    ======   ")
        print("  ==         ==    ========    =====     ==    =====     ==    ==         ==    == ")
        print("  ==    =    ==       ==       ==  ==    ==    ==  ==    ==    ==         ======   ")
        print("  ==  == ==  ==       ==       ==   ==   ==    ==   ==   ==    =======    ====     ")
        print("  == ==   == ==       ==       ==    ==  ==    ==    ==  ==    ==         ==  ==   ")
        print("  ===       ===    ========    ==     =====    ==     =====    ==         ==    == ")
        print("   =         =     ========    ==      ====    ==      ====    =======    ==     ==")

        print("")
        print("=================================>>>>> (^_^) <<<<<=================================")
        print("")
        if num == guessnum:
            print("")
            print("          Play Again")
            print("")
            con = input("Press Y to continue OR N to exit : ")
            print("")
            if con == 'y' or con == 'Y':
                print("     New Game ==>>")
                print("")
                i = 0
                chance = 5
                print("Total Chance :  ", chance)
                print("")
            elif con == 'n' or con == 'N':
                break
            else:
                break

    else:
        chance -= 1
        print("Wrong Number.")
        print("")
        print("Chance Left :  ", chance)
        print("")

    if chance == 0:
        print("=======================>>>>>- YOU LOOSE -<<<<<==========================")
        print("==                                                                    ==")

        print("==  ==               =====            ====    =======    ======       ==")
        print("==  ==             ==     ==       ==         ==         ==    ==     ==")
        print("==  ==           ==         ==    ==          ==         ======       ==")
        print("==  ==           ==         ==      ====      =======    ====         ==")
        print("==  ==            ==       ==           ==    ==         ==  ==       ==")
        print("==  =========      ==     ==           ==     ==         ==    ==     ==")
        print("==  =========        =====        ====        =======    ==     ==    ==")

        print("==                                                                    ==")
        print("=======================>>>>>- YOU LOOSE -<<<<<==========================")

    if chance == 0:
        print("")
        print("          Play Again")
        print("")
        con = input("Press Y to continue OR N to exit : ")
        print("")
        if con == 'y' or con == 'Y':
            print("     New Game ==>>")
            print("")
            i = 0
            chance = 5
            print("Total Chance :  ", chance)
            print("")
        elif con == 'n' or con == 'N':
            break
        else:
            break

    i += 1

input("Press Enter to exit the Game.")
