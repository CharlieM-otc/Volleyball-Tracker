#Ask user if it is tracking information for a junior or semior volleyball game
game_type = input("Is this a junior (3 set) or senior (5 set) game?").lower().strip()
try:
    if game_type == "junior":
        set_number == 3
    elif game_type == "senior":
        set_number == 5
except NameError:
    print("Something went wrong. Please try again.")
