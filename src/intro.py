from utils.alerts import show_alert

intros = [
	'Welcome to Space Junk Collector!',
	'''
There\'s a lot of space junk/garbage orbiting Earth.
	''',
	'''
Collect the junk by shooting bullets.
Level up when there is no more junk

Move left and right by pressing/holding the
left or right arrow keys, or 'A' and 'D'

Shoot by pressing 'W", 'space', or the 'Up' arrow key
	'''
]

# def onclick():
# 	show_alert('There\'s a lot of garbage orbiting Earth. \nShoot the garbage and level up', level_up, 500)

def start_intro(callback, index = -1):
	def show_intro():
		nonlocal index
		index += 1

		if index < len(intros):
			show_alert(intros[index], show_intro, 500)
		else:
			callback()

	show_intro()
