import turtle

screen = turtle.Screen()
screen.bgcolor('#000000')
screen.title('Space Garbage Collector')

# game state
ready = False

def show_alert(message, width = 200, text_color = 'white', box_color = 'red'):
	box = turtle.Turtle()

	# center box
	(x, y) = turtle.screensize()

	box.speed(0)
	box.penup()
	box.goto(-x + width / 4, -(width / 4))
	box.pendown()

	# draw shape
	box.color(box_color)
	box.begin_fill()
	box.hideturtle()

	for i in range(4):
		if i % 2: box.forward(width / 2)
		else: box.forward(width)

		box.left(90)

	box.end_fill()
	
	# go to center of message box and write text
	box.forward(width / 2)
	box.left(90)
	box.forward(width / 4)

	# write text
	box.color(text_color)
	box.write(
		message,
		font=('San Serif', 16, 'normal'),
		align='center'
	)

