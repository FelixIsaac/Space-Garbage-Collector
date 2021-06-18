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

def left():
	global x
	(collector_x, collector_y) = collector.position()

	if collector_x - 50 < -x: return

	collector.penup()
	collector.goto(collector_x - 30, collector_y)
	collector.pendown()

def right():
	global x
	(collector_x, collector_y) = collector.position()
	
	if collector_x + 50 > x: return

	collector.penup()
	collector.goto(collector_x + 30, collector_y)
	collector.pendown()

def show():
	collector.showturtle()
