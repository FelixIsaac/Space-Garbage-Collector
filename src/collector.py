from playsound import playsound
from turtle import Turtle, screensize

(x, y) = screensize()

collector = Turtle()
collector.speed(0)
collector.hideturtle()
collector.penup()
collector.goto(0, -y + 20)

collector.pendown()
collector.shape('./assets/collector.gif')
collector.penup()

collector_bullet = Turtle(shape='arrow', visible=False)
collector_bullet.speed(3)
collector_bullet.shapesize(.5, 1)
collector_bullet.color('yellow')
collector_bullet.penup()
collector_bullet.setheading(90)

def left():
	global x
	(collector_x, collector_y) = collector.position()
	if collector_x <= -x: return


	collector.goto(collector_x - 30, collector_y)

def right():
	global x
	(collector_x, collector_y) = collector.position()
	if collector_x >= x: return
	
	collector.goto(collector_x + 30, collector_y)

def shoot():
	if collector_bullet.isvisible(): return

	playsound('./assets/audio/shoot.mp3', block=False)
	(collector_x, collector_y) = collector.position()

	collector_bullet.speed(0)
	collector_bullet.setposition(collector_x, collector_y + 20)
	collector_bullet.showturtle()
	collector_bullet.speed(3)

def bullet_movement(speed = 2):
	collector_bullet.forward(speed)

	if collector_bullet.ycor() > y:
		collector_bullet.hideturtle()

def bullet_collided_with(junk):
	return collector_bullet.distance(junk) < (20 + junk.width() + 1)

def is_bullet_visible():
	return collector_bullet.isvisible()

def destroy_bullet():
	collector_bullet.hideturtle()

def show():
	collector.showturtle()
