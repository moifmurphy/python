drink = ["Pepsi", "Cherry Coke Zero", "Sprite"]
crisps = ["Monster Munch", "Wotsits", "Skips"]
chocolate = ["Snickers", "Double Decker", "Bounty"]

while True:
    choice = input("Would you like a DRINK, some CRISPS or some CHOCOLATE? ").lower()
    if choice == 'drink':
        snack = drink.pop()
    elif choice == 'crisps':
        snack = crisps.pop()
    elif choice == 'chocolate':
        snack = chocolate.pop()
    else:
        print("Sorry I didn't understand that.")
        continue
    print("here's your {}: {}".format(choice, snack))