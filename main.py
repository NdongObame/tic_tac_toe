gpo = {1: " ", 2: " ", 3: " ",
       4: " ", 5: " ", 6: " ",
       7: " ", 8: " ", 9: " "
       }


def gb():
    board = ("I " + gpo[1] + " I " + gpo[2] + " I " + gpo[3] + " I" +
             "\nI " + gpo[4] + " I " + gpo[5] + " I " + gpo[6] + " I" +
             "\nI " + gpo[7] + " I " + gpo[8] + " I " + gpo[9] + " I")
    return board


print('''
I 1 I 2 I 3 I 
I 4 I 5 I 6 I 
I 7 I 8 I 9 I 
''')

option = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def turn(player):
    playturn = input("which place do you want to play:")
    while playturn not in option:
        playturn = input("not available input. which place do you want to play:")
    option.remove(playturn)
    gpo[int(playturn)] = player
    print(gb())


def winner():
    w1 = gpo[1] + gpo[2] + gpo[3]
    w2 = gpo[4] + gpo[5] + gpo[6]
    w3 = gpo[7] + gpo[8] + gpo[9]
    w4 = gpo[1] + gpo[5] + gpo[9]
    w5 = gpo[3] + gpo[5] + gpo[7]
    w6 = gpo[1] + gpo[4] + gpo[7]
    w7 = gpo[2] + gpo[5] + gpo[8]
    w8 = gpo[3] + gpo[6] + gpo[9]

    if w1 == "XXX" or w2 == "XXX" or w3 == "XXX" or w4 == "XXX" or \
            w5 == "XXX" or w6 == "XXX" or w7 == "XXX" or w8 == "XXX":
        print("player 2 wins ")
        G = "n"
        return G
    elif w1 == "OOO" or w2 == "OOO" or w3 == "OOO" or w4 == "OOO" or \
            w5 == "OOO" or w6 == "OOO" or w7 == "OOO" or w8 == "XXX":
        print("player 1 wins ")
        G = "n"
        return G
    else:
        G = "y"
        return G


p1 = "O"
p2 = "X"
g = "y"
import random

first = random.randrange(1, 3)
if first == 1:
    print("player 1 start")
    while g == "y" and len(option) != 0:
        print("player 1")
        turn(p1)
        g = winner()
        if g == "y" and len(option) != 0:
            print("player 2")
            turn(p2)
            g = winner()
elif first == 2:
    print("player 2 start")
    while g == "y" and len(option) != 0:
        print("player 2")
        turn(p2)
        g = winner()
        if g == "y" and len(option) != 0:
            print("player 1")
            turn(p1)
            g = winner()

if len(option) == 0 and g =="y":
    print("its a tie")