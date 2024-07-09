import random
import math

def mathGame(targets: list[str]):
    num1, oper, num2 = random.randrange(0, 10), targets[random.randrange(0, len(targets)-1)], random.randrange(0, 10)
    ans = str(num1) + str(oper) + str(num2)
    print("solve this problem " + ans + ", it's rounded down", end="\n")
    while True:
        num3 = input("enter the answer here : ")
        if int(num3) == int(eval(ans)):
            return num3 + " is correct\n" 
        print(num3 + " is not correct, try again", end="\n")
play = True
while play == True:
    print(mathGame(["+", "/", "*", "-"]))
    target = input("play again(y/n)")
    if target == "y" or target == "Y":
        play = True
    else: 
        play = False
print("thanks for playing")