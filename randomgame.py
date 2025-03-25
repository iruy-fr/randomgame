from random import randint
guessing = randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    try:
        if 0 <int(guess) < 11:
            if guessing == guess:
                print("Correct!")
                break
            pass
    except ValueError:
        print("That's not an integer.")
        continue