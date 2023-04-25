import turtle

# set up game window
window = turtle.Screen()
window.title("Pong Game")
window.setup(width=800, height=600)
window.bgcolor("black")
window.tracer(0) # disable automatic tracer, to updated only when screen objects are ready

# set player1 object
player1 = turtle.Turtle()
player1.speed(0) # set frames to max
player1.goto(-350,0) # set screen position of player1 object
player1.penup() # stop moving objects from drawing lines
player1.shape("square")
player1.color("red")
player1.shapesize(stretch_wid=5, stretch_len=1) 

# set player2 object
player2 = turtle.Turtle()
player2.speed(0) # set frames to max
player2.goto(350,0) # set screen position of player2 object
player2.penup() # stop moving objects from drawing lines
player2.shape("square")
player2.color("blue")
player2.shapesize(stretch_wid=5, stretch_len=1) 

# set ball object
ball = turtle.Turtle()
ball.speed(0) # set frames to max
ball.goto(0,0) # set initial screen position of ball object
ball.penup() # stop moving objects from drawing lines
ball.shape("circle")
ball.color("yellow")
ball.dx = 0.5
ball.dy = 0.5

# set border object
border = turtle.Turtle()
border.speed(0) # set frames to max
border.goto(0,0)  # set screen position of border object
border.shape("square")
border.color("white")
border.shapesize(stretch_wid=23, stretch_len=0.1) 

# set score panel object
score = turtle.Turtle()
score.speed(0) # set frames to max
score.goto(0,260)  # set screen position of score board object
score.color("white")
score.hideturtle() # display text only
score.penup()
player1_score = 0
player2_score = 0

# set game over panel object
game_over = turtle.Turtle()
def initialize_game_over_panel():    
    game_over.speed(0) # set frames to max
    game_over.goto(0,0)  # set screen position of game over object
    game_over.color("white")
    game_over.hideturtle() # display text only
    game_over.penup()

# set player movements
def player_up(player):
    y = player.ycor()
    if player.ycor() >= 250:
        return
    y += 20
    player.sety(y)

def player_down(player):
    y = player.ycor()
    if player.ycor() <= -250:
        return
    y -= 20
    player.sety(y)

# respond to keyboard events
window.listen()
window.onkeypress(lambda: player_up(player1), "w") # moving player1 up when (w) is pressed
window.onkeypress(lambda: player_down(player1), "s") # moving player1 down when (s) is pressed
window.onkeypress(lambda: player_up(player2), "Up") # moving player2 up when (Up arrow) is pressed
window.onkeypress(lambda: player_down(player2), "Down") # moving player2 down when (Down arrow) is pressed


# game loop
while True:
    window.update()

    # update bal position
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # border check
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >= 390:
        ball.goto(0,0)
        ball.dx *= -1
        player1_score += 1
    
    if ball.xcor() <= -390:
        ball.goto(0,0)
        ball.dx *= -1
        player2_score += 1

    # collesion check
    if(ball.xcor() >= 340 and ball.xcor() <= 350) and (ball.ycor() <= player2.ycor()+40 and ball.ycor() >= player2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() <= -340 and ball.xcor() >= -350) and (ball.ycor() <= player1.ycor()+40 and ball.ycor() >= player1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1

    # display updated score
    score.clear()
    score.write("Player 1: {}  Player 2: {}".format(player1_score,player2_score), align="center", font=("Courier", 17, "normal"))

    # check if final score is reached, first player reaching 3 points wins
    if player1_score == 3:
        window.reset()
        initialize_game_over_panel()
        game_over.write("Player 1 wins!", align="center", font=("Courier", 24, "normal"))
        turtle.mainloop()

    elif player2_score == 3:
        window.reset()
        initialize_game_over_panel()
        game_over.write("Player 2 wins!", align="center", font=("Courier", 24, "normal"))
        turtle.mainloop()

        
