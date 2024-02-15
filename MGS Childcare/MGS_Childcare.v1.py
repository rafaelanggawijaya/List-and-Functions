def dropoff():
    while True:
        name = input("Please enter your child's name: ").title()
        if name != name.strip():
            print("Please enter a Valid answer")
        else:
            roll.append(name)
            print(f"This child, {name} has been added to the list")
            break


def pickup():
    while True:
        pick_kid = input("What is the name of the child "
                         "you want to pick up: ").title()
        if pick_kid not in roll:
            print(f"{pick_kid} is not on the list.")
        else:
            roll.remove(pick_kid)
            print(f"{pick_kid} has been removed from the list.")
            break


def calccost():
    hours = int(input("How many hours has your child/s been here?: "))
    child_count = int(input("How many children do you wish to pick up?: "))
    print(f"Your cost is ${hours * child_count * 12} ")


def printroll():
    print(", ".join(roll))


# Main routine
choice = 0
roll = []
while choice != 5:
    print("---------------------------------------------------------------"
          "-------")

    print("Welcome to MGS Childcare")

    print("What would you like to do? Please "
          "choose one of the items below")

    print("---------------------------------------------------------------"
          "--------")

    print()

    print("1 Drop off a child")

    print("2 Pick up a child")

    print("3 Calculate cost")

    print("4 Print roll")

    print("5 Exit the system")

    print()

    choice = int(input("Enter your choice (number between 1 and 5): "))

    print()

    if choice == 1:

        dropoff()

    elif choice == 2:

        pickup()

    elif choice == 3:

        calccost()

    elif choice == 4:

        printroll()

    else:
        print("Goodbye")
