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
ready = True
garbages = []
level = 0
development = False

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
	global level
	level += 1

	if level == 1: player.show()

	create_garbage(3 * level)

if not development: start_intro(level_up)
else: level_up()

screen.onkeypress(player.left, 'Left')
screen.onkeypress(player.right, 'Right')
screen.listen()

screen.mainloop()
