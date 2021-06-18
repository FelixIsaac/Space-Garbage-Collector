from turtle import Turtle, screensize

(x, y) = screensize()

collector = Turtle()
collector.speed(0)
collector.hideturtle()
collector.penup()
collector.goto(0, -y + 20)

collector.pendown()
collector.shape('square')
collector.color('green')
collector.shapesize(3, 5)
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

	(collector_x, collector_y) = collector.position()

	collector_bullet.speed(0)
	collector_bullet.setposition(collector_x, collector_y + 20)
	collector_bullet.showturtle()
	collector_bullet.speed(3)

def bullet_movement():
	collector_bullet.forward(10)

	if collector_bullet.ycor() > y:
		collector_bullet.hideturtle()

def bullet_collided_with(junk):
	return collector_bullet.distance(junk) < (20 + junk.width() + 1)

def is_bullet_visible():
	return collector_bullet.isvisible()

def show():
	collector.showturtle()
