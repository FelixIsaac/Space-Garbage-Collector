import random
from turtle import Screen, Turtle, screensize
from utils.alerts import show_alert
from intro import start_intro
import collector as player

screen = Screen()
screen.bgcolor('#000000')
screen.bgpic('./assets/background.gif')
screen.title('Space Garbage Collector')

# game state
ready = False
garbages = []
level = 0
development = True

def create_garbage(garbages_num):
	(x, y) = screensize()

	for i in range(garbages_num):
		randomX = random.randint(-x, x)
		randomY = random.randint(-7, y)
		randomWidth = random.uniform(0.5, 1.5)
		randomHeight = random.uniform(0.5, 1.5)

		garbage = Turtle()
		garbage.speed(0)
		garbage.hideturtle()
		garbage.color('red')
		garbage.shape('circle')
		garbage.penup()
		garbage.shapesize(randomWidth, randomHeight)
		garbage.goto(randomX, randomY)
		garbage.showturtle()

		garbages.append(garbage)

def level_up():
	global level, ready

	ready = True
	level += 1

	if level == 1: player.show()

	create_garbage(3 * level)

if not development: start_intro(level_up)
else: level_up()

screen.onkeypress(lambda: player.left() if ready else None, 'a')
screen.onkeypress(lambda: player.left() if ready else None, 'Left')

screen.onkeypress(lambda: player.right() if ready else None, 'd')
screen.onkeypress(lambda: player.right() if ready else None, 'Right')

screen.onkey(lambda: player.shoot() if ready else None, 'w')
screen.onkey(lambda: player.shoot() if ready else None, 'Up')
screen.onkey(lambda: player.shoot() if ready else None, 'space')
screen.listen()

def game():
	player.bullet_movement()

	screen.update()
	screen.ontimer(game, 50)

game()
screen.mainloop()
