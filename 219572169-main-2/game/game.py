import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass

    number = random.randint(1, n)


    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            if number < guess:
                print("Too large!")
            elif number > guess:
                print("Too small!")
            elif number == guess:
                print("Just right!")
                break

        except ValueError:
            pass



main()
