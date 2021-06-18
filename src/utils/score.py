from turtle import Turtle, screensize

(x, y) = screensize()

score = Turtle()
score.speed(0)
score.shape('square')
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, y)

def update_scoreboard(points, level):
	FONT=("Courier", 24, "normal")
	
	score.clear()
	score.write("Points: {} Level: {}".format(points, level), align="center", font=FONT)
