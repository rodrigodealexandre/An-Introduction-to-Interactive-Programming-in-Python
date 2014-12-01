# template for "Stopwatch: The Game"
import simplegui
# define global variables

win_time = 0
wins = 0
tries = 0
t = 0
running = False

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global win_time, t, running
    time.start()
    win_time = (win_time + 1)%10
    t = t + 1
    running = True

def reset():
    global tries, wins, t, win_time, running
    win_time = 0
    wins = 0
    tries = 0
    t = 0
    running = False
    time.stop()

def stop():
    global tries, wins, running
    if running == True and win_time == 0:
        wins += 1
        tries += 1
        running = False
        time.stop()
    elif running == True:
        tries += 1
        time.stop()
        running = False
        
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d = t%10
    c = (t/10)%10
    b = (t/100)%6
    a = t/10/60
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handler for timer with 0.1 sec interval
time = simplegui.create_timer(100, start)

# define draw handler
def draw(c):
    c.draw_text(format(t),[50, 80], 35, "White")
    c.draw_text(str(wins) + " / " + str(tries),[160, 15], 15, "Yellow")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 150)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)


# start frame
frame.start() 



###################################################
# Test code for the format function
# Note that function should always return a string with 
# seven characters
print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)

###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9