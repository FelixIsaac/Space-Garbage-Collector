import random
from turtle import Screen, Turtle, screensize
from utils.alerts import show_alert
from utils.score import update_scoreboard
from intro import start_intro
import collector as player

screen = Screen()
screen.bgcolor('#000000')
screen.bgpic('./assets/background.gif')
screen.title('Space Junk Collector')

# game state
development = False
ready = False
level = 0
score = 0
junk_list = []

def create_junk(num_of_junk):
	(x, y) = screensize()

	for i in range(num_of_junk):
		randomX = random.randint(-x, x)
		randomY = random.randint(-7, y)
		randomWidth = random.uniform(0.5, 1.5)
		randomHeight = random.uniform(0.5, 1.5)

		junk = Turtle()
		junk.speed(0)
		junk.hideturtle()
		junk.color('red')
		junk.shape('circle')
		junk.penup()
		junk.shapesize(randomWidth, randomHeight)
		junk.goto(randomX, randomY)
		junk.showturtle()

		junk_list.append(junk)

def level_up():
	global level, ready

	ready = True
	level += 1

	if level == 1: player.show()

	update_scoreboard(score, level)
	create_junk(3 * level)

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
	global score, level

	if player.is_bullet_visible():
		player.bullet_movement()

		for index, junk in list(enumerate(junk_list)):
			if player.bullet_collided_with(junk):
				junk.clear()
				junk.hideturtle()
				junk_list.remove(junk)
				
				score += 1
				update_scoreboard(score, level)

			if len(junk_list) == 0:
				# no more junk, level up!
				player.destroy_bullet()
				level_up()

	screen.update()
	screen.ontimer(game, 50)

game()
update_scoreboard(score, level)
screen.mainloop()
