# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

       



# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

 

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        for crds in self.hand:
            hc = hc + str(crds)
        return hc
    
    def add_card(self, card):
        self.hand.append(card)


    def get_value(self):
        card_value = 0
        ace = False
        for count in range(0, len(self.hand)):
            card_value += VALUES[self.hand[count].rank]
            if self.hand[count].rank == 'A':
                ace = True
        if ace and card_value + 10 <= 21:
            card_value += 10
        return card_value 
        
    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + 45
        if hidden == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [181,250], CARD_BACK_SIZE)
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(str(suit),str(rank)))
        self.shuffle()
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
    
    def card_ammount(self):
        return len(self.deck)    

    def deal_card(self):
        self.deal = self.deck[-1]
        self.deck.pop()
        
        return self.deal
        
    
     
    


#define event handlers for buttons

def start():
    global deck, in_play, score, hidden, outcome
    global blackjack, scoring, outcome2
    deck = Deck()
    in_play = False
    score = 0
    hidden = True
    outcome = ""
    outcome2 = "New deal?"
    blackjack = False
    scoring = False
    
def deal():
    global outcome, in_play, player1, dealer, deck, hidden 
    global score, text, blackjack, scoring, outcome, outcome2
    outcome = ""
    outcome2 = "Hit or stand?"
    if scoring == True:
        score -= 1
    scoring = True
    in_play = True
    blackjack = False
    text = "Black"
    deck = Deck()
    hidden = True
    player1 = Hand()
    dealer = Hand()
    player1.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player1.add_card(deck.deal_card())
    if hidden == True: 
        if player1.get_value() == 21:
            blackjack = True
            hidden = False
            outcome = "Black Jack, player wins."
            score += 1
            scoring = False
            outcome2 = "New deal?"
            return outcome
        dealer.add_card(deck.deal_card())
        
    
    

    
def hit():
    global text, hidden, blackjack, outcome
    global score, scoring, outcome2
    
    if in_play == False:
        deal()
    
    
    elif hidden == True and player1.get_value() <= 21:
        player1.add_card(deck.deal_card())
        if player1.get_value() > 21:
            text = "Red"
            hidden = False
            score -= 1
            outcome = "Player busted. Dealer Wins."
            scoring = False
            outcome2 = "New deal?"
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global hidden, score, in_play, outcome, scoring, outcome2
    if in_play == False:
        deal()
    hidden = False
    if player1.get_value() > 22 and scoring == True:
        score -= 1
        outcome = "Player busted. Dealer Wins."
        outcome2 = "New deal?"
        scoring = False
    if blackjack == False:
        if player1.get_value() < 22:
            while player1.get_value() > dealer.get_value():
                dealer.add_card(deck.deal_card())
                if dealer.get_value() > 21:
                    score += 1
                    outcome = "Dealer busted. Player Wins."
                    outcome2 = "New deal?"
                    scoring = False
        if dealer.get_value() > player1.get_value() and dealer.get_value() <= 21 and scoring == True:
            score -= 1
            outcome = "Dealer Wins."
            outcome2 = "New deal?"
            scoring = False 
        if dealer.get_value() == player1.get_value() and dealer.get_value() <= 21 and scoring == True: 
            score -= 1
            outcome = "Dealer Wins on ties."
            outcome2 = "New deal?"
            scoring = False             
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

    
image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')



# draw handler    
def draw(canvas):
    
     
    # test to make sure that card.draw works, replace with your code below
    if in_play == True:
        dealer.draw(canvas, [100, 200])    
        player1.draw(canvas, [100, 400])
        canvas.draw_text("Player sum " + str(player1.get_value()), [450, 400], 18, text)
    
    if hidden == False:    
        canvas.draw_text("Dealer sum " + str(dealer.get_value()), [450, 200], 18, "Black")
    
    if blackjack == True:
        canvas.draw_text(outcome, [300, 150], 30, "Black")
    
    if blackjack == False:
        canvas.draw_text(outcome, [270, 150], 30, "Black")
    
    canvas.draw_text(outcome2, [200, 360], 22, "Black")
    canvas.draw_text("Dealer cards:", [10, 250], 16, "Black")
    canvas.draw_text("Player cards:", [10, 450], 16, "Black")
    canvas.draw_text("Black Jack",[200,50],40,"Black")
    
    for i in range(deck.card_ammount()): 
        canvas.draw_image(card_back, (71/2, 96/2), (71, 96), (40+i*4, 120), (71, 96))
    
    canvas.draw_text("Score " + str(score), [480, 50], 30, "Black")
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)

frame.add_button("New Game", start, 200)
frame.set_draw_handler(draw)


# get things rolling
start()
frame.start()


# remember to review the gradic rubric