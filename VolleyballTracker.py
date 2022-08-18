#Ask the user to if it is a junior or senior game
number_of_sets = 0
team_a_point_score = 0
team_b_point_score = 0
shirt_list_team_a = []
shirt_list_team_b = []
team_a_set_score = 0
team_b_set_score = 0
team_a_number_of_subs = 12
team_b_number_of_subs = 12

game_type = input("Is the game a junior (best of 3 sets) game or a senior (best of 5 sets) game?").strip().lower()
if game_type == "junior":
    number_of_sets += 3
if game_type == "senior":
    number_of_sets += 5

#Ask the users for the names of the teams playinng
team_a = input("What is the name of the team that is team A?")
team_b = input("What is the name of the team that is team B?")

#Ask the user for the shirt numbers of the players of on the court for each team
for i in range(7):
    shirt_number_input_team_a = input("Please enter the shirt number of a person on the court for " + team_a)
    shirt_list_team_a.append(shirt_number_input_team_a)

for i in range(7):
    shirt_number_input_team_b = input("Please enter the shirt number of a person on the court for " + team_b)
    shirt_list_team_b.append(shirt_number_input_team_b)

#Display the shirt numbers on the court
print("The players on the court for {} are: {}".format(team_a, shirt_list_team_a))
print("The players on the court for {} are: {}".format(team_b, shirt_list_team_b))

#Display action menu to user and allow user to commence a action as many times as they want
while True:
    action = int(input("Action menu: Enter the number which correspondes to the action you are wishing to take. '1' = add  a point. '2' = remove a point. '3' = make a substitution. '4' = call a timeout. '5' = add a set. '6' = exit program."))
    #Adding a point
    if action == 1:
        which_team = input("Which team won the point: if team A ({}) won the point enter 'A'. If team B ({}) won the pont enter 'B'. If you wish to go back to the menu enter 'back'.".format(team_a, team_b))
        if which_team == "A":
            team_a_point_score += 1
            print("Points: {} = {}. {} = {}.".format(team_a, team_a_point_score, team_b, team_b_point_score))
            print("Sets: {} = {}. {} = {}".format(team_a, team_a_set_score, team_b, team_b_set_score))
            print("Player's shirt numbers who are on the court: {} = {}. {} = {}".format(team_a, shirt_list_team_a, team_b, shirt_list_team_b))
        elif which_team == "B":
            team_b_point_score += 1
            print("Points: {} = {}. {} = {}.".format(team_a, team_a_point_score, team_b, team_b_point_score))
            print("Sets: {} = {}. {} = {}".format(team_a, team_a_set_score, team_b, team_b_set_score))
            print("Player's shirt numbers who are on the court: {} = {}. {} = {}".format(team_a, shirt_list_team_a, team_b, shirt_list_team_b))
        elif which_team == "back":
            print("Going back to menu.")
            print("Points: {} = {}. {} = {}.".format(team_a, team_a_point_score, team_b, team_b_point_score))
            print("Sets: {} = {}. {} = {}".format(team_a, team_a_set_score, team_b, team_b_set_score))
            print("Player's shirt numbers who are on the court: {} = {}. {} = {}".format(team_a, shirt_list_team_a, team_b, shirt_list_team_b))
        else:
            print("An error has occured, please try again.")
    #Removing a point
    elif action == 2:
        which_team = input("Which team are you removing a point from: if team A ({}) enter 'A'. If team B ({}) enter 'B'. If you wish to go back to the menu enter 'back'.".format(team_a, team_b))
        if which_team == "A":
            team_a_point_score -= 1
            print("Points: {} = {}. {} = {}.".format(team_a, team_a_point_score, team_b, team_b_point_score))
            print("Sets: {} = {}. {} = {}".format(team_a, team_a_set_score, team_b, team_b_set_score))
            print("Player's shirt numbers who are on the court: {} = {}. {} = {}".format(team_a, shirt_list_team_a, team_b, shirt_list_team_b))
        elif which_team == "B":
            team_b_point_score -= 1
            print("Points: {} = {}. {} = {}.".format(team_a, team_a_point_score, team_b, team_b_point_score))
            print("Sets: {} = {}. {} = {}".format(team_a, team_a_set_score, team_b, team_b_set_score))
            print("Player's shirt numbers who are on the court: {} = {}. {} = {}".format(team_a, shirt_list_team_a, team_b, shirt_list_team_b))
        elif which_team == "back":
            print("Going back to menu.")
            print("Points: {} = {}. {} = {}.".format(team_a, team_a_point_score, team_b, team_b_point_score))
            print("Sets: {} = {}. {} = {}".format(team_a, team_a_set_score, team_b, team_b_set_score))
            print("Player's shirt numbers who are on the court: {} = {}. {} = {}".format(team_a, shirt_list_team_a, team_b, shirt_list_team_b))
        else:
            print("Am error has occured, please try again.")

     #Making a substitution *THIS IS NOT WORKING*
    elif action == 3:
        which_team = input("Which team is making a substitution: if team A ({}) enter 'A'. If team B ({}) enter 'B'. If you wish to go back to the menu enter 'back'.".format(team_a, team_b))
        if which_team == "A":
            current_shirt_number = int(input("What number is being subbed off the court?"))
            replacement_shirt_number = int(input("What number is being subbed on the court?"))
            shirt_list_team_a.get(current_shirt_number)
            shirt_list_team_a.remove(current_shirt_number)
            shirt_list_team_a.append(replacement_shirt_number)


