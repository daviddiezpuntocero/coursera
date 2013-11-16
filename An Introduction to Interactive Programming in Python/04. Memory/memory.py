# implementation of card game - Memory

import simplegui
import random

CARD_NUMBER  = 16
FRAME_WIDTH  = 800
FRAME_HEIGHT = 100
CARD_WIDTH   = FRAME_WIDTH/CARD_NUMBER
CARD_HEIGHT  = FRAME_HEIGHT
# Set debug to True to debug when do the peer programing
DEBUG        = False
FONT_SIZE    = 20

def is_debug():
    return True == DEBUG

def init_globals():
    global turn, cards, exposed, pre_exposed_card_idx, \
    cur_exposed_card_idx, state
    cards = range(CARD_NUMBER/2)
    cards.extend(range(CARD_NUMBER/2))
    random.shuffle(cards)
    exposed = [False for i in range(0, CARD_NUMBER)]
    state   = 0  
    turn = 0

# helper function to initialize globals
def new_game():
    init_globals()  
    label.set_text("Turns = " + str(turn))    
    
def show_card(num):
    global exposed, pre_exposed_card_idx, cur_exposed_card_idx    
    exposed[num] = True
    pre_exposed_card_idx = cur_exposed_card_idx
    cur_exposed_card_idx = num    

def change_card_display(new_status):
    exposed[cur_exposed_card_idx] = new_status
    exposed[pre_exposed_card_idx] = new_status
    
def update_turn():
    global turn
    turn += 1
    label.set_text("Turns = " + str(turn))
    
# define event handlers
def mouseclick(pos):
    global exposed, state, pre_exposed_card_idx, cur_exposed_card_idx
    num = pos[0]/CARD_WIDTH
    if is_debug():
        print "Card ", num, "Clicked, number is", cards[num], "State is ", state
    if False == exposed[num]:        
        if state == 1:
            update_turn()                                            
            show_card(num)
            state = 2
        elif state == 0:
            exposed[num] = True
            cur_exposed_card_idx = num
            state = 1
        elif state == 2:
            if cards[cur_exposed_card_idx] == cards[pre_exposed_card_idx]:
                change_card_display(True)
            else:
                change_card_display(False)
            show_card(num)       
            state = 1           
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed
    for i in range(CARD_NUMBER):
        if True == exposed[i]:
            canvas.draw_polygon([[CARD_WIDTH*i, 0], \
                                 [CARD_WIDTH*(i+1), 0], \
                                 [CARD_WIDTH*(i+1), CARD_HEIGHT], \
                                 [CARD_WIDTH*i, CARD_HEIGHT]], 1, \
                                'White', 'Black')            
            canvas.draw_text(str(cards[i]), \
                             (CARD_WIDTH*i + CARD_WIDTH/2, CARD_HEIGHT/2), \
                             FONT_SIZE, 'White', 'serif')
        
        else:
            canvas.draw_polygon([[CARD_WIDTH*i, 0], \
                                 [CARD_WIDTH*(i+1), 0], \
                                 [CARD_WIDTH*(i+1), CARD_HEIGHT], \
                                 [CARD_WIDTH*i, CARD_HEIGHT]], 1, \
                                'White', 'Green')
            if is_debug():
                canvas.draw_text(str(i) + ":" + str(cards[i]), \
                                 (CARD_WIDTH*i + 15, 25), 10, 'White', 'serif')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", FRAME_WIDTH, FRAME_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
