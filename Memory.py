# implementation of card game - Memory

import simplegui
import random





# helper function to initialize globals
def new_game():
    
    global cards, exposed, state, moves, choices, pos1
    pos1 = [50,100]
    state = 0
    cards = range(0,8)+ range(0,8)
    random.shuffle(cards)
    exposed = [True]*16
    choices=[-1,-1]
    moves = 0
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state,  moves, choices
    for mouse in range(16):
        if pos[0] >= (pos1[0] * mouse) and pos[0] <= (pos1[0] * (mouse + 1)):
            if exposed[mouse] == True:
                exposed[mouse] = False
                if state == 0:
                    choices[0] = mouse; state = 1
                elif state == 1:
                    choices[1] = mouse; state = 2
                    moves += 1                    
                elif state == 2:
                    state = 1
                    if cards[choices[0]] != cards[choices[1]]:
                        exposed[choices[0]] = True
                        exposed[choices[1]] = True
                    choices[0] = mouse
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    for index in range(16):
        if exposed[index] == True:
            canvas.draw_polygon([(pos1[0] * index, 0), (pos1[0] * (index + 1), 0), (pos1[0] * (index + 1), pos1[1]), (pos1[0] * index, pos1[1])], 2, "White", "Green")
        elif exposed[index] == False:
            canvas.draw_polygon([(pos1[0] * index, 0), (pos1[0] * (index + 1), 0), (pos1[0] * (index + 1), pos1[1]), (pos1[0] * index, pos1[1])], 2, "White", "Yellow")
            number_position = [((pos1[0] * index + 25)-10), pos1[0]+15]
            canvas.draw_text(str(cards[index]), number_position, 45, "Blue")
        
            
    label.set_text("Moves = "+str(moves))
    
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric