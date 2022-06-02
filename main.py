import random

choice = ("r", "s", "p")


def user_selected_option():
    while True:
        user = input("Enter an option: ")
        if user.lower() not in choice:
            print("Please provide an acceptable value")
        else:
            return user
            break


user_option = user_selected_option()
cpu = random.choice(choice)

while True:
    if user_option == cpu:
        print("Sorry, select again there was a tie")
        user_option = user_selected_option()
        cpu = random.choice(choice)
    else:
        if user_option == "r" and cpu == "s":
            print("You win")
        elif user_option == "p" and cpu == "r":
            print("You win")
        elif user_option == "s" and cpu == "p":
            print("You win")
        elif cpu == "r" and user_option == "s":
            print("You loose")
        elif cpu == "p" and user_option == "r":
            print("You loose")
        else:
            print("You loose")

        break
