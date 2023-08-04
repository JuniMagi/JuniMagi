import random
def bot():
    a = (int(random.randrange(1,4)))
    if a == 1:
        print ("Computer Picked Rock")
        return 1
    elif a == 2:
        print ("Computer Picked Paper")
        return 2
    elif a == 3:
        print ("Computer Picked Scissors")
        return 3
    else :
        print("cpfail")
def playerin():
    x = 0
    while x == 0:
        a = input("Rock, Paper or Scissors? ")
        if a == "Rock":
            print("You picked Rock")
            print("vs")
            x = 1
        elif a == "Paper" :
            print("You picked Paper")
            print("vs")
            x = 2
        elif a == "Scissors":
            print("You picked Scissors")
            print("vs")
            x = 3
        else : 
            print("Invalid")
    return x

def main():
    y = playerin()
    x = bot()
    if x == y:
        print("It's a tie!")
    elif (x == 1 and y == 2) or (x == 2 and y == 3 ) or (x == 3 and y == 1):
        print("Playerwin")
        return "xwin"
    else:
        print('Computerwin')
        return "ywin"

def wincon():
    gameover=False
    Pscore = 0
    Bscore = 0
    while not gameover:
        s = main()
        if s == "xwin":
            Pscore += 1
            print("again")
            print("Player Score: " , Pscore)
            print("Bot Score: ", Bscore)
        elif s =="ywin":
            Bscore += 1
            print("again")
            print("Player Score: " , Pscore)
            print("Bot Score: ", Bscore)
        else:
            Pscore += 1
            Bscore += 1
            print("again")
            print("Player Score: " , Pscore)
            print("Bot Score: ", Bscore)
        if Bscore >= 5 :
            print("Bot win")
            gameover = True
        elif Pscore >= 5 :
            print("Player win")
            gameover = True


wincon()
input()
