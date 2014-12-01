# starting point for calculator
import simplegui
# intialize globals
store = 0
operand = 0

# event handlers for calculator with a store and operand
# define functions that manipulate store and operand


def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""
def swap():
    global store, operand
    store, operand = operand, store
    output()
def add():
    global store, operand
    store = store + operand
    output()
def sub():
    global store, operand
    store = store - operand
    output()
def mult():
    global store, operand
    store = store * operand
    output()
def div():
    global store, operand
    if operand == 0:
        print "Can't divide by Zero"
        print " "
    else:
        store = store / operand
        output()
def clear():
    global store, operand
    store = 0
    operand = 0
    output()

def enter(e):
    global operand
    """
    float() gives you the chance to have desimals,
    int() its just full numbers
    str() is text
    """
    operand = float(e)
    output()
    
# create frame
frame = simplegui.create_frame("Calculator", 200,300)


# register event handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)
frame.add_button("Clear", clear, 100)
frame.add_input("Enter operand N.", enter, 100)

# get frame rolling
frame.start()