# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
direction = "LEFT"
score1 = 0
score2 = 0

dir = 0

ball_vel = [0,0]



paddle1_vel = [0]
paddle2_vel = [0]



# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    if direction is "RIGHT":
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        ball_vel[0] = -2.0
        ball_vel[1] = -2.0
    elif direction is "LEFT":
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        ball_vel[0] = 2.0
        ball_vel[1] = -2.0
    
     

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    
    paddle1_pos = [0, HEIGHT/2 ]
    paddle2_pos = [0, HEIGHT/2 ]
    
    
    spawn_ball(direction)    
  
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, vel, direction
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT,paddle1_pos[1] + HALF_PAD_HEIGHT,1): 
        ball_vel[0] = -ball_vel[0] 
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    if ball_pos[0] <= 13:
        direction = "RIGHT"
        score2 = score2 + 1
        spawn_ball(direction)
        
        
            
    if int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and int(ball_pos[1]) in range(paddle2_pos[1] - HALF_PAD_HEIGHT,paddle2_pos[1] + HALF_PAD_HEIGHT,1):  
        ball_vel[0] = -ball_vel[0] 
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    if ball_pos[0] >= 587:
        direction = "LEFT"
        score1 = score1 + 1
        spawn_ball(direction)
        
        
    
    if (ball_pos[1] <= (0 + BALL_RADIUS)) or (ball_pos[1] >= (HEIGHT - 1 - BALL_RADIUS)):
        ball_vel[1] = -ball_vel[1]
            
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS,1,"White", "White")
   
    # update paddle's vertical position, keep paddle on the screen
    print paddle1_pos[1]
    
    paddle1_pos[1] += paddle1_vel[0]
    paddle2_pos[1] += paddle2_vel[0]
    
    if paddle1_pos[1] <= 40 or paddle1_pos[1] >=360:
        paddle1_vel[0] = 0
        if paddle1_pos[1] < 40:
            paddle1_pos[1] = 40
        if paddle1_pos[1] > 360:
            paddle1_pos[1] = 360
        
    if paddle2_pos[1] <= 40 or paddle2_pos[1] >=360:
        paddle2_vel[0] = 0
        if paddle2_pos[1] < 40:
            paddle2_pos[1] = 40
        if paddle2_pos[1] > 360:
            paddle2_pos[1] = 360
     
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos[1] - HALF_PAD_HEIGHT),
                                   (PAD_WIDTH -2, paddle1_pos[1] - HALF_PAD_HEIGHT), 
                                   (PAD_WIDTH -2, paddle1_pos[1] + HALF_PAD_HEIGHT), 
                                   (0, paddle1_pos[1] + HALF_PAD_HEIGHT)], 
                                   PAD_WIDTH, "White")
    canvas.draw_polygon([(600, paddle2_pos[1] - HALF_PAD_HEIGHT),
                                   (600 + 2 - PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT), 
                                   (600 + 2 - PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT), 
                                   (600, paddle2_pos[1] + HALF_PAD_HEIGHT)], 
                                   PAD_WIDTH, "White")
    # draw scores
    canvas.draw_text(str(score1),[WIDTH/4, 80], 35, "White")
    canvas.draw_text(str(score2),[WIDTH*3/4, 80], 35, "White")
        
        
        
        
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= paddle2_vel[0] +5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] += paddle2_vel[0] +5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] -= paddle1_vel[0] +5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] += paddle1_vel[0] +5   

    
def keyup(key):
    
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= paddle2_vel[0]
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] -= paddle2_vel[0]
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] -= paddle1_vel[0]
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] -= paddle1_vel[0] 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New", new_game, 50)


# start frame
new_game()
frame.start()
