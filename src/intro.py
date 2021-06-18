from utils.alerts import show_alert
from app import level_up

def onclick():
	show_alert('There\'s a lot of garbage orbiting Earth. \nShoot the garbage and level up', level_up, 500)

show_alert('Welcome to Space Garbage Collector!', onclick, 500)
