#Ask the user to if it is a junior or senior game
number_of_sets = 0
team_a = "a"
team_b = "b"
team_a_point_score = 0
team_b_point_score = 0
shirt_list_team_a = []
shirt_list_team_b = []
team_a_set_score = 0
team_b_set_score = 0
team_a_number_of_subs = 12
team_b_number_of_subs = 12
team_a_timeouts = 3
team_b_timeouts = 3

#Printing info function
def game_info():
    print("Going back to menu.")
    print("Points: {} = {}. {} = {}.".format(team_a, team_a_point_score, team_b, team_b_point_score))
    print("Sets: {} = {}. {} = {}".format(team_a, team_a_set_score, team_b, team_b_set_score))
    print("Player's shirt numbers who are on the court:\n {} = {}.\n {} = {}".format(team_a, shirt_list_team_a, team_b, shirt_list_team_b))

#Get number of sets in this game - game type
correct = False
while correct == False:
    game_type = input("Is the game a junior (best of 3 sets) game or a senior (best of 5 sets) game?\n").strip().lower()
    if game_type == "junior":
        number_of_sets += 3
        correct = True
    elif game_type == "senior":
        number_of_sets += 5
        correct = True
    else:
        print("An error has occured please try again. Make sure to double check what you are doing.")

#Ask the users for the names of the teams playinng
valid = False
while valid == False:
    team_a = input("What is the name of the team that is team A?\n")
    team_b = input("What is the name of the team that is team B?\n")
    if team_b == team_a:
        print("You have entered the same team name for both teams. Try again.")
    else:
        valid = True

#Ask the user for the shirt numbers of the players of on the court for each team
for i in range(7):
    okay = True
    while okay == True:
        shirt_number_input_team_a = input("Please enter the shirt number of a person on the court for " + team_a + "\n")
        different = shirt_number_input_team_a in shirt_list_team_a
        if different == True:
            print("This player number has already been entered.")
        else:
            shirt_list_team_a.append(shirt_number_input_team_a)
            different = False
            okay = False

for i in range(7):
    okay = True
    while okay == True:
        shirt_number_input_team_b = input("Please enter the shirt number of a person on the court for " + team_b + "\n")
        different = shirt_number_input_team_b in shirt_list_team_b
        if different == True:
            print("This player number has already been entered.")
        else:
            shirt_list_team_b.append(shirt_number_input_team_b)
            different = False
            okay = False

#Display the shirt numbers on the court
print("The players on the court for {} are:\n {}".format(team_a, shirt_list_team_a))
print("The players on the court for {} are:\n {}".format(team_b, shirt_list_team_b))

#Display action menu to user and allow user to commence a action as many times as they want
while True:
    action = int(input("Action menu: Enter the number which correspondes to the action you are wishing to take.\n'1' = add a point.\n'2' = remove a point.\n'3' = make a substitution.\n'4' = call a timeout.\n'5' = add a set.\n'6' = exit program.\n"))
    #Adding a point
    if action == 1:
        which_team = input("Which team won the point: if team A ({}) won the point enter 'A'. If team B ({}) won the pont enter 'B'. If you wish to go back to the menu enter 'back'.\n".format(team_a, team_b))
        if which_team == "A" or which_team == 'a':
            team_a_point_score += 1
            game_info()
        elif which_team == "B" or which_team == 'b':
            team_b_point_score += 1
            game_info()
        elif which_team == "back" or which_team == 'Back':
            game_info()
        else:
            print("An error has occured, please try again.")
    #Removing a point
    elif action == 2:
        which_team = input("Which team are you removing a point from: if team A ({}) enter 'A'. If team B ({}) enter 'B'. If you wish to go back to the menu enter 'back'.".format(team_a, team_b))
        if which_team == "A" or which_team == "a":
            if team_a_point_score == 0:
                print(team_a + " has 0 points. You can not remove a point.")
            else:
                team_a_point_score -= 1
            game_info()
        elif which_team == "B" or which_team == "b":
            if team_a_point_score == 0:
                print(team_b + " has 0 points. You can not remove a point.")
            else:
                team_b_point_score -= 1
            game_info()
        elif which_team == "back" or which_team == 'Back':
            print("Going back to menu.")
            game_info()
        else:
            print("An error has occured, please try again.")

     #Making a substitution
    elif action == 3:
        which_team = input("Which team is making a substitution: if team A ({}) enter 'A'. If team B ({}) enter 'B'. If you wish to go back to the menu enter 'back'.".format(team_a, team_b))
        if which_team == "A" or which_team == 'a':
            current_shirt_number = input("What number is being subbed off the court?")
            replacement_shirt_number = input("What number is being subbed on the court?")
            for i in range(7):
                if shirt_list_team_a[i] == current_shirt_number:
                    shirt_list_team_a[i] = replacement_shirt_number
            game_info()
        elif which_team == "B" or which_team == 'b':
            current_shirt_number = input("What number is being subbed off the court?")
            replacement_shirt_number = input("What number is being subbed on the court?")
            for i in range(7):
                if shirt_list_team_b[i] == current_shirt_number:
                    shirt_list_team_b[i] = replacement_shirt_number
            game_info()
        elif which_team == "back" or which_team == 'Back':
            print("Going back to menu.")
            game_info()
        else:
            print("An error has occured. Please try again.")

    #Calling a timeout
    if action == 4:
        which_team = input("If team A ({}) is calling a timeout enter: 'A'. If team B ({}) is calling a timeout enter: 'B'. If you want to go back to menu enter: 'back'".format(team_a, team_b))
        #Team A calling a timeout
        if which_team == "A" or which_team == 'a':
            #Check they haven't already used all of their timeouts
            if team_a_timeouts == 0:
                print(team_a + " is out of timeouts.")
                game_info()
            elif team_a_timeouts > 0:
                team_a_timeouts -= 1
                #Inform the coaches - keep them updated and informed
                if team_a_timeouts == 2:
                    print("Team A ({}) has {} remaining timeouts, please tell their coach this.".format(team_a, team_a_timeouts))
                    game_info()
                elif team_a_timeouts == 1:
                    print("Team A ({}) has {} remaining timeouts, please tell their coach this.".format(team_a, team_a_timeouts))
                    game_info()
                elif team_a_timeouts == 0:
                    print("Team A ({}) is out of timeouts, please tell their coach.".format(team_a))
                    game_info()

        #Team B calling a timeout
        elif which_team == "B" or which_team == 'b':
            #Check they haven't already used all of their timeouts
            if team_b_timeouts == 0:
                print(team_b + " is out of timeouts.")
                game_info()
            elif team_b_timeouts > 0:
                team_b_timeouts -= 1
                #Inform the coaches - keep them updated and informed
                if team_b_timeouts == 2:
                    print("Team B ({}) has {} remaining timeouts, please tell their coach this.".format(team_b, team_b_timeouts))
                    game_info()
                elif team_a_timeouts == 1:
                    print("Team B ({}) has {} remaining timeouts, please tell their coach this.".format(team_b, team_b_timeouts))
                    game_info()
                elif team_a_timeouts == 0:
                    print("Team B ({}) is out of timeouts, please tell their coach.".format(team_b))
                    game_info()

        #Going back to menu
        elif which_team == "back" or which_team == 'Back':
            print("Going back to menu.")

        else:
            print("An error has occured, please try again.")

    #Adding a set
    if action == 5:
        #Make sure the information is written down
        print("Write down the score for the last set:\n Team A ({}) points = {}.\n Team B ({}) points = {}.".format(team_a, team_a_point_score, team_b, team_b_point_score))
        which_team = input("If Team A ({}) won the set enter: 'A'. If Team B ({}) won the set enter: 'B'. If you wish to go back to the menu enter: 'back'".format(team_a, team_b))

        #Team A won the set *CHECK*
        if which_team == "A" or which_team == 'a':
            team_a_set_score += 1
            if number_of_sets == 3:
                if team_a_set_score == 2:
                    print("Team A ({}) has won! The set score was: Team A ({}) = {} and Team B ({}) = {}.".format(team_a, team_a, team_a_set_score, team_b, team_b_set_score))
                    break
                else:
                    print("The set score is: Team A ({}) = {} and Team B ({}) = {}.".format(team_a, team_a_set_score, team_b, team_b_set_score))
                    team_a_point_score = 0
                    team_b_point_score = 0

            if number_of_sets == 5:
                    if team_a_set_score == 3:
                        print("Team A ({}) has won! The set score was: Team A ({}) = {} and Team B ({}) = {}.".format(team_a, team_a, team_a_set_score, team_b, team_b_set_score))
                        break
                    else:
                        print("The set score is: Team A ({}) = {} and Team B ({}) = {}.".format(team_a, team_a_set_score, team_b, team_b_set_score))
                        team_a_point_score = 0
                        team_b_point_score = 0

        if which_team == "B" or which_team == 'b':
            team_b_set_score += 1
            if number_of_sets == 3:
                if team_b_set_score == 2:
                    print("Team B ({}) has won! The set score was: Team A ({}) won {} sets. Team B ({}) won {} sets.".format(team_b, team_a, team_a_set_score, team_b, team_b_set_score))
                    break
                else:
                    print("The set score is: Team A ({}) = {} and Team B ({}) = {}.".format(team_a, team_a_set_score, team_b, team_b_set_score))
                    team_a_point_score = 0
                    team_b_point_score = 0

            if number_of_sets == 5:
                if team_b_set_score == 3:
                    print("Team B ({}) has won! The set score was: Team A ({}) won {} sets. Team B ({}) won {} sets.".format(team_b, team_a, team_a_set_score, team_b, team_b_set_score))
                    break
                else:
                    print("The set score is: Team A ({}) = {} and Team B ({}) = {}.".format(team_a, team_a_set_score, team_b, team_b_set_score))
                    team_a_point_score = 0
                    team_b_point_score = 0

        if which_team == 'back' or which_team == 'Back':
            print("Going back to menu.")

    #Exiting the program
    if action == 6:
        leaving =  input("Are you sure you wish to exit the program, all the stored information will be lost. Enter 'stay' to stay in the program and enter 'leave' to leave the program.").strip().lower()
        #staying
        if leaving == 'stay' or leaving == 'Stay':
            print("Going back to menu.")

        #exiting program
        elif leaving == 'leave' or leaving == 'Leave':
            print("Leaving program.")
            break

        #mistake made
        else:
            print("An error has occured, please try again.")

