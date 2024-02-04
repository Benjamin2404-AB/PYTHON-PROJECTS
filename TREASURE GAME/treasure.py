print("Welcome to the treasure game!! Your mission is to find the treasure")

path = input("Where do you want to go? L or R ? \n")


if path == "L":
    path2 = input("You have arrived at a lake. Do you want to swim or wait?\n")
    if path2 == "Swim":
        print("Game Over you drowned")
    elif path2 == "Wait":
        path3 = input("You waited for a ferry and crossed to a building on an Island. Which Door will you take ? : Red , Blue or Yellow? \n")
        if path3 == "Red" or "Blue":
            print("Game Over!! You lost")
        else:
            print("You won !!! You found the Treasure")