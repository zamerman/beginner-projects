import random
choice = 'yes'

def game():
    guesses = 0
    # assigns a random number 
    number = random.randint(1,100) 
    while True:
        n = int(input("Guess the number "))
        if n == number:
            guesses += 1
            print("You guessed correctly, the number was ", n)
            print("You took ", guesses," guesses ")
            choice = input('Play again? ').lower()
            if choice == 'yes' or choice == 'y':
                game()
            else:
                    break
            
        elif n < number:
            print("Try higher Numbers\n ")
            guesses += 1
        else:
            print("Try lower Numbers \n")
            guesses += 1
game()
