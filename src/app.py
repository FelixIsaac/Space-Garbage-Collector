import random
from turtle import Screen, Turtle, screensize 
from utils.alerts import show_alert

screen = Screen()
screen.bgcolor('#000000')
screen.title('Space Garbage Collector')

# game state
ready = True
garbages = []
level = 0

def create_garbage(garbages_num):
	(x, y) = screensize()

	for i in range(garbages_num):
		randomX = random.randint(-x, x)
		randomY = random.randint(-y, y)
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

	create_garbage(3 * level)

def onclick():
	show_alert('There\'s a lot of garbage orbiting Earth. \nShoot the garbage and level up', level_up, 500)

show_alert('Welcome to Space Garbage Collector!', onclick, 500)

while True:
	screen.update()
