import turtle
import paddle
import ball
import scoreboard
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")


player_1 = turtle.textinput("Player 1", "Enter the name of player 1, arrow-up for UP & arrow-down for DOWN")
player_2 = turtle.textinput("Player 2", "Enter the name of Player 2, 'w' for UP & 's' for DOWN")
target = turtle.numinput("Score Target", "Enter your score target?", minval=1)
winner = ""

paddle_r = paddle.Paddle(350,0)
paddle_l = paddle.Paddle(-350,0)

ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

screen.listen()
turtle.onkey(paddle_r.up, "Up")
turtle.onkey(paddle_r.down, "Down")
turtle.onkey(paddle_l.up, "w")
turtle.onkey(paddle_l.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_back()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_r_score()

    if scoreboard.r_score == target:
        game_is_on = False
        winner = player_1

    if scoreboard.l_score == target:
        game_is_on = False
        winner = player_2

scoreboard.teleport(0,-50)
scoreboard.write(f"Winner is: {winner}", font=("Courier", 18, "normal"), align="center")

screen.exitonclick()