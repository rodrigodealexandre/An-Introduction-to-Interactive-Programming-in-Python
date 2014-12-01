# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # 
    if name == "rock":
        return 0
    elif name == "Spock":
        return  1
    elif name == "paper":
        return  2
    elif name == "lizard":
        return  3
    elif name == "scissors":
        return  4
    elif name not in ("rock","Spock", "lizard","paper", "scissors"):
        return random.randrange(0,5)
    
def number_to_name(number):
    # 
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
   
    

import random
def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    name_to_number(player_choice) 

    # compute random guess for comp_number using random.randrange()
    ramdom = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_number = number_to_name(ramdom)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_number

    # compute difference of comp_number and player_number modulo five
    diff = (name_to_number(player_choice) - ramdom)%5
     
    # use if/elif/else to determine winner, print winner message
    
    if (player_choice not in ("rock","Spock","paper","lizard","scissors")):
        print "%s is not a valid choice, so computer wins!"% player_choice              
    elif diff == 0:
        print "Player and computer tie!"
    elif diff <= 2:
        print "Player wins!"
    elif diff >= 3:
        print "Computer wins!"           

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


