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
LEFT = False
RIGHT = True
LINE_COLOR = "Red"
FILL_COLOR = "Red"
BALL_LINE_WIDTH = 1
PAD_LINE_WIDTH = 1
PAD_VEL = 5
VEL_INCRE = 0.1
SCORE_TEXT_COLOR = "Gray"

paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

def limit_val(value, max, min):
    if value > max:
        return [max, True]
    elif value < min:
        return [min, True]
    else:
        return [value, False]
    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    h_vel = random.randrange(120, 240) / 60
    v_vel = -random.randrange(60, 180) / 60
    if LEFT == direction:
        ball_vel = [-h_vel, v_vel]
    elif RIGHT == direction:
        ball_vel = [h_vel, v_vel]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1]]
            
    # draw ball
    if ((ball_pos[1] >= paddle1_pos - PAD_HEIGHT/2 - BALL_RADIUS) \
            and (ball_pos[1] <= paddle1_pos + PAD_HEIGHT/2 + BALL_RADIUS) \
            and (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS)) \
         or ((ball_pos[1] >= paddle2_pos - PAD_HEIGHT/2 - BALL_RADIUS) \
             and (ball_pos[1] <= paddle2_pos + PAD_HEIGHT/2 + BALL_RADIUS) \
             and (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS)): # hit the paddle
        [ball_pos[0], swap_x] = limit_val(ball_pos[0], 
                                          WIDTH - BALL_RADIUS - PAD_WIDTH, 
                                          BALL_RADIUS + PAD_WIDTH)        
        ball_vel = [ball_vel[0] * (1 + VEL_INCRE), ball_vel[1] * (1 + VEL_INCRE)]
        ball_vel[0] = - ball_vel[0]        
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH: # right guy miss the paddle
        spawn_ball(LEFT)        
        score1 = score1 + 1
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH: # left guy miss the paddle
        spawn_ball(RIGHT)
        score2 = score2 + 1
  
    [ball_pos[1], swap_y] = limit_val(ball_pos[1], HEIGHT - BALL_RADIUS, BALL_RADIUS)
    if (swap_y):
        ball_vel[1] = - ball_vel[1]
        
    c.draw_circle((ball_pos[0], ball_pos[1]), 
                  BALL_RADIUS, BALL_LINE_WIDTH, LINE_COLOR, FILL_COLOR)
    
    # update paddle's vertical position, keep paddle on the screen
    [paddle1_pos, swap] = limit_val(paddle1_pos + paddle1_vel, HEIGHT - PAD_HEIGHT/2, PAD_HEIGHT/2)
    [paddle2_pos, swap] = limit_val(paddle2_pos + paddle2_vel, HEIGHT - PAD_HEIGHT/2, PAD_HEIGHT/2)   
    
    # draw paddles
    c.draw_polygon([[0, paddle1_pos - PAD_HEIGHT/2],
                    [PAD_WIDTH, paddle1_pos - PAD_HEIGHT/2],
                    [PAD_WIDTH, paddle1_pos + PAD_HEIGHT/2],
                    [0, paddle1_pos + PAD_HEIGHT/2]],
                   PAD_LINE_WIDTH, LINE_COLOR, FILL_COLOR)    
    c.draw_polygon([[WIDTH, paddle2_pos - PAD_HEIGHT/2],
                    [WIDTH - PAD_WIDTH, paddle2_pos - PAD_HEIGHT/2],
                    [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT/2],
                    [WIDTH, paddle2_pos + PAD_HEIGHT/2]],
                   PAD_LINE_WIDTH, LINE_COLOR, FILL_COLOR)       
    
    # draw scores
    c.draw_text(str(score1), (150, 100), 72, SCORE_TEXT_COLOR)
    c.draw_text(str(score2), (450, 100), 72, SCORE_TEXT_COLOR)
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -PAD_VEL
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -PAD_VEL          
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = PAD_VEL              
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = PAD_VEL
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
    elif (key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0              

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()
