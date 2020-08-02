'''If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''
from random import randint
ans = randint(0,100)
guesses = [0]
roundcount = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    try:
        guess=int(guess)
        if type(guess) == int:
            if int(guess) < 1 or int(guess) > 100:
                guess = int(guess)
                print ("OUT OF BOUNDS")
                continue
            else:
                guess = int(guess)
                guesses.append(guess)
                if guess == ans:
                    print ("CONGRATS!")
                    break
                elif roundcount<1 and abs(ans - guess)<10:
                    print("WARM!")
                elif roundcount<1 :
                    print("COLD!")

                if roundcount>=1 and guess == ans:
                    print ("CONGRATS!")
                    break
                elif roundcount>=1 and abs(guesses[-1] - ans) < abs(guesses[-2] - ans):
                    print("Warmer!")
                    continue
                elif roundcount>=1:
                    print("Colder!")
                    continue
                else:
                    pass
                roundcount += 1
    except ValueError:
        print("try again")
        pass

    pass
