from turtle import Turtle, screensize, onscreenclick

def draw_rect(turtle, width, height):
	positions = []

	for i in range(4):
		positions.append(turtle.pos())

		if i % 2: turtle.forward(height)
		else: turtle.forward(width)

		turtle.left(90)

	return positions

def show_alert(message, button_click, width = 200, text_color = 'white', box_color = 'red'):
	box = Turtle()

	# center box
	(x, y) = screensize()

	box.speed(0)
	box.penup()
	box.goto(-x + width / 4, -(width / 4))
	box.pendown()
	box.hideturtle()

	# draw shape
	box.color(box_color)
	box.begin_fill()
	draw_rect(box, width, width / 2)
	box.end_fill()
	
	# go to center of message box and write text
	box.penup()
	box.forward(width / 2)
	box.left(90)
	box.forward(width / 4)
	box.pendown()

	# write text
	box.color(text_color)
	box.write(
		message,
		font=('San Serif', 16, 'normal'),
		align='center'
	)
	
	# Button
	button_width = 150
	button_height = 30
	
	# center button
	box.right(180)
	box.penup()
	box.forward((width / 4) - (button_height + 10))
	box.right(90)
	box.forward(-(width / 8))
	box.pendown()

	# Draw button
	box.color('white')
	box.begin_fill()
	button_positions = draw_rect(box, button_width, button_height)
	box.end_fill()

	# go to center of button and write text
	box.penup()
	box.forward(button_width / 2)
	box.left(90)
	box.forward(button_width / 5)
	box.pendown()

	# Write button text
	box.color('black')
	box.write(
		'Continue',
		font=('San Serif', 16, 'normal'),
		align='center'
	)

	# listen for button click
	def check_button_click(x, y):
		if (
			x >= button_positions[1][0] and x <= button_positions[0][0]
			and y >= button_positions[2][1] and y <= button_positions[0][1]
		):
			# clear dialoge and button listener
			onscreenclick(None)
			box.reset()

			button_click()

	onscreenclick(check_button_click, 1)
