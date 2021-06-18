import turtle
import random
from utils.alerts import show_alert

screen = turtle.Screen()
screen.bgcolor('#000000')
screen.title('Space Garbage Collector')

# game state
ready = False

# screen.textinput("Welcoem to Space Garbage Collector", "There's a lot of garbage orbiting Earth")

def onclick():
	print('Hello world! User clicked on button')

show_alert('Welcome to Space Garbage Collector!', onclick, 200)

def create_garbage(garbages):
	(x, y) = turtle.screensize()

	for i in range(garbages):
		randomX = random.randint(-x, x)
		randomY = random.randint(-y, y)
		randomWidth = random.uniform(0.5, 1.5)
		randomHeight = random.uniform(0.5, 1.5)

		garbage = turtle.Turtle()
		garbage.speed(0)
		garbage.hideturtle()
		garbage.color('red')
		garbage.shape('circle')
		garbage.penup()
		garbage.shapesize(randomWidth, randomHeight)
		garbage.goto(randomX, randomY)

input('')
# while True:
# 	pen
