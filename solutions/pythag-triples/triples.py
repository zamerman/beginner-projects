# Pythagorean Triples Checker
# Python 3.5.1
# Written by alfredmuffin

def loop():
    play = input("Would you like to play again? (y/n) "),lower()
    if play == "n":
        print("\nGoodbye!")
        break
    else:
        print("I didn't quite catch that.")
        loop()


while True:
    side_1 = int(input("Enter a side: ")) ** 2
    side_2 = int(input("Enter another side: ")) ** 2
    side_3 = int(input("Enter another side: ")) ** 2

    statement = "\nThis is a pythagorean triple."
    not_statement = "\nThis is not a pythagorean triple."

    triangle = [side_1, side_2, side_3]
    hypotenuse = max(triangle)

    triangle.remove(hypotenuse)

    if sum(triangle) == hypotenuse:
        print(statement)
    else:
        print(not_statement)
    
    loop()
