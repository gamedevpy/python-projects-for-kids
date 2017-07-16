#!/usr/bin/env python2
##------------------------------------------------------
##
## By: Jessica Ingrassellino
## Publisher: Packt Publishing
## Pub. Date: April 14, 2016
## Web ISBN-13: 978-1-78528-585-1
## Print ISBN-13: 978-1-78217-506-3
##
## Python Projects for Kids
## Chapter 8 - pygame
##
##------------------------------------------------------

# imported libraries go here
import pygame
import time

SLEEP_SECONDS = 1 ## Number of seconds to pause

## Global variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

CIRCLE_RADIUS = 10
CIRCLE_X = 250
CIRCLE_Y = 300

RECT_X = 20
RECT_Y = 30
RECT_HEIGHT = 50
RECT_WIDTH = 90

pygame.init()

screen_width = 400
screen_height = 600	
game_screen = pygame.display.set_mode((screen_width, screen_height))
game_screen.fill(black)

while True:
	time.sleep(SLEEP_SECONDS)
	pygame.draw.circle(game_screen, red, (CIRCLE_X, CIRCLE_Y), CIRCLE_RADIUS)
	pygame.draw.rect(game_screen, blue, (RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT))
	pygame.draw.ellipse(game_screen, white, (300, 200, 40, 80))
	

	## Animation
	if CIRCLE_RADIUS > 1:
		CIRCLE_RADIUS = CIRCLE_RADIUS + 10
		print("Attempting to shrink the circle")

	RECT_Y = RECT_Y + 40

	pygame.display.update()