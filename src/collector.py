import threading
from playsound import playsound
from turtle import Turtle, screensize

(x, y) = screensize()

class Collector(Turtle):
	def __init__(self):
		super().__init__()

		self.speed(0)
		self.hideturtle()
		self.penup()
		self.goto(0, -y + 20)

		self.pendown()
		self.shape('./assets/collector.gif')
		self.penup()

	def left(self):
		global x
		(collector_x, collector_y) = self.position()
		if collector_x <= -x: return


		self.goto(collector_x - 30, collector_y)

	def right(self):
		global x
		(collector_x, collector_y) = self.position()
		if collector_x >= x: return
		
		self.goto(collector_x + 30, collector_y)

	def show(self):
		self.showturtle()

class Bullet(Turtle):
	def __init__(self):
		super().__init__(shape='arrow', visible=False)
		self.speed(3)
		self.shapesize(.5, 1)
		self.color('yellow')
		self.penup()
		self.setheading(90)

	def move(self, speed = 2):
		self.forward(speed)

		if self.ycor() > y:
			self.hideturtle()

	def playeffect(self):
		thread = threading.Thread(target = lambda: playsound('./assets/audio/shoot.mp3', block=False), name = 'soundThread')
		thread.start()

	def shoot(self, collector_cors):
		if self.isvisible(): return

		self.playeffect()
		(collector_x, collector_y) = collector_cors

		self.speed(0)
		self.setposition(collector_x, collector_y + 20)
		self.showturtle()
		self.speed(3)

	def collided_with(self, junk):
		return self.distance(junk) < (20 + junk.width() + 1)

	def destroy(self):
		self.hideturtle()
