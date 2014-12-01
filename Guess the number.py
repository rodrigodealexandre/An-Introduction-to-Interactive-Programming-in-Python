# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# initialize global variables used in your code

num_range = 100
n_guess = 7
game_type = 100

# helper function to start and restart the game

def new_game():
    global game_type
    
    if game_type == 100: 
        range100()
    elif game_type == 1000:
        range1000()

    
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    global n_guess
    global game_type
    game_type = 100
    n_guess = 7
    num_range = random.randrange(0,101)
    print ""
    print "--------------------------------"
    print "New game. Range is from 0 to 100"
    print "You have " + str(n_guess)+ " chances."
    print ""
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    global n_guess
    global game_type
    game_type = 1000
    n_guess = 10
    num_range = random.randrange(0,1001)
    print ""
    print "--------------------------------"
    print "New game. Range is from 0 to 1000"
    print "You have " + str(n_guess)+ " chances."
    print ""
        
def input_guess(guess):
    # main game logic goes here	
    global num_range
    global n_guess
    n_guess = n_guess - 1 
    
    if int(n_guess) == 0 and int(guess) != int(num_range):
        print "Your guess was ", int(guess)
        print "Sorry, you lose. The number was " + str(num_range) + "." 
        print "Let's start a new game..."
        print " "
        
    elif int(n_guess) == 0 and int(guess) == int(num_range):
        print "Your guess was ", int(guess)
        print "Well done!"
        print "You got it in your last try!"
        print "Let's start a new game..."
        n_guess = -1
        print " "
    
    elif int(n_guess) < 0 :
        new_game()
    
    elif int(guess) == int(num_range):
        print "Your guess was ", int(guess)
        print "Well done!"
        print "You still had " + str(n_guess) + " more guesses."
        print "Let's start a new game..."
        n_guess = -1
        print " "
        
    elif int(guess) > int(num_range):
        print "Your guess was ", int(guess)
        print "You still have " + str(n_guess) + " more guesses."
        print "Lower!"
        print " "
        
    elif int(guess) < int(num_range):
        print "Your guess was ", int(guess)
        print "You still have " + str(n_guess) + " more guesses."
        print "Higher!"
        print " "
    
        
# create frame
frame = simplegui.create_frame("Guess the number", 300,200)


# register event handlers for control elements
frame.add_button("Range is [0 to 100]", range100, 200)
frame.add_button("Range is [0 to 1000]", range1000, 200)
frame.add_input("Enter your guess number",input_guess,200)

new_game()

# call new_game and start frame
frame.start()


# always remember to check your completed program against the grading rubric
