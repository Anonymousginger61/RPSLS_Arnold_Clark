# Callum Inglis
# Arnold Clark Hack Day
# Python 2.7.16
# 2019/05/25

import random

# Here are the different actions that can be performed
# The action above the next is the greater power. i.e. Paper beats Rock
actions = ['Scissors',
           'Paper',
           'Rock',
           'Lizard',
           'Spock',
           'Scissors',
           'Lizard',
           'Paper',
           'Spock',
           'Rock']

# Get all unique actions that can be performed (Convert the list to a set to remove duplicates)
unique_actions = list(set(actions))

# Return a list of indexes where this action appears in the actions list
def get_indexs(action):
    action_index = []
    for i in range(len(actions)):
        if (actions[i] == action):
            action_index.append(i)

    return action_index

# Main Method: Rock, Paper, Scissors, Lizard, Spock!
def RPSLS():
    # What the user chooses (e.g. Scissiors)
    user_action = raw_input("Enter Action: ")

    # Check that this is a valid action (i.e. it appears at least once in the actions list)
    if (actions.count(user_action) > 0):

        # Get the index(s) of this (user) action in the actions list
        user_action_list = get_indexs(user_action)

        # Choose a random action for the other move
        computer_action = actions[random.randint(0, len(actions) - 1)]
        print "Computer Action: " + computer_action
        
        # Get the index(s) of this (computer) action in the actions list
        computer_action_list = get_indexs(computer_action) 

        # For each user action, check if this wins/looses against the computer action
        for i in user_action_list:
            for j in computer_action_list:
                #print " > " + actions[i] + " Vs " + actions[j] # Debugging to show comparisons

                # Check for a wraparound as the the bottom action can beat the top action (Rock Vs Scissors)
                if (i + 1 == len(actions)): user_compare = 0
                else: user_compare = i+1
                    
                if (j + 1 == len(actions)): computer_compare = 0
                else: computer_compare = j+1

                # If user action is one before the computer action, user wins
                if (user_compare == j):
                    print "You Win! " + user_action + " beats " + computer_action + "\n\n"
                    return RPSLS()

                # If computer action is one before the user action, user looses
                elif (computer_compare == i):
                    print "You Loose. " + computer_action + " beats " + user_action + "\n\n"
                    return RPSLS()

        print "Draw. Going around again...\n\n"
        return RPSLS()

    else:
        print "Sorry, the action " + user_action + " is not valid. The following actions are allowed: \n -",
        for unique in unique_actions:
            print unique + ",",
        print "\nGoing around again...\n\n"
        return RPSLS()

# GO! Call the function again each time we get to a result
print "Rock, Paper, Scissors, Lizard, Spock!\nCallum Inglis - www.calluminglis.com\nPython 2.7.16\n"

print RPSLS()
