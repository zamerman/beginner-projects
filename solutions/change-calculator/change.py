# Change Calculator
# Python 3.5.1
# Written by alfredmuffin

# dollar values per type of coin
pennyValue = 0.01
nickelValue = 0.05
dimeValue = 0.1
quarterValue = 0.25

continue = True

# request input
while continue:
    print("Welcome to the change calculator!")

    price = float(input("What is the price of the item? $"))
    money = float(input("What is the amount of money given to you? $"))

    # calculate total value of change needed
    targetChange = money - price
    print("Change needed is ${0}".format(targetChange))

    quarters = int(targetChange / quarterValue)
    targetChange -= quarters * quarterValue

    dimes = int(targetChange / dimeValue)
    targetChange -= dimes * dimeValue

    nickels = int(targetChange / nickelValue)
    targetChange -= nickels * nickelValue

    pennies = int(targetChange / pennyValue)
    targetChange -= pennies * pennyValue

    print("\t{} quarters".format(quarters))
    print("\t{} dimes".format(dimes))
    print("\t{} nickels".format(nickels))
    print("\t{} pennies\n".format(pennies))
    continue = input("To go again press 0:)


print("Goodbye!")
