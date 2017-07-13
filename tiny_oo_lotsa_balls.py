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
## Chapter 9 - Tiny Tennis
##
##------------------------------------------------------

# imports, globals and drawing

# imported libraries go here
import time
import pygame
import random
import math
import sys

sys.path.append('./lib')

from Color.Helper import Helper
from TinyTennis.Ball import Ball
from TinyTennis.Paddle import Paddle
from TinyTennis.Screen import Screen
from TinyTennis.ScoreKeeper import ScoreKeeper

color_helper = Helper()

NUMBER_BALLS = 1

ball_uid = 1

ball_dict = {}

BALL_RADIUS   = 10
BALL_VELOCITY = 5

BALL_COLOR    = color_helper.getWhite()
COURT_COLOR   = color_helper.getBlack()
PADDLE_COLOR  = color_helper.getBlue()
NET_COLOR     = color_helper.getYellow()
SCORE_TEXT_COLOR = color_helper.getWhite()

screen = Screen(800, 500)

score_keeper = ScoreKeeper()

# screen globals
screen_width  = screen.getWidth()
screen_height = screen.getHeight()

def create_ball(i):

	ball = Ball(int(screen_width / 2), int(screen_height / 2), BALL_VELOCITY, BALL_VELOCITY, BALL_RADIUS)

	ball.setScreenHeight(screen_height)

	ball.setScreenWidth(screen_width)

	global ball_uid

	ball_uid += 1

	ball.setId(ball_uid)

	global ball_dict

	ball_dict[ball_uid] = ball


def initialize_balls(num_balls):

	for i in range(num_balls):
	
		print("Processing %d" % i)

		create_ball(i)


def point_scored():

	global NUMBER_BALLS
	
	NUMBER_BALLS += 1
	
	initialize_balls(NUMBER_BALLS)
	
	for ball_id in ball_dict:
	
		ball = ball_dict[ball_id]

		ball.serve()


def remove_ball(ball_id):

	global ball_dict

	if ball_id in ball_dict:	
		del ball_dict[ball_id]
	else:
		print("ball with id %d does not exist" % ball_id)


# initialize pygame
pygame.init()

game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tiny Tennis")
font = pygame.font.SysFont("monospace", 75)

initialize_balls(NUMBER_BALLS)

paddle1 = Paddle(10, 10, 25, 100)
paddle1.setScreenHeight(screen_height)

paddle2 = Paddle(screen_width - 35, 10, 25, 100)
paddle2.setScreenHeight(screen_height)

pygame.mouse.set_visible(0)

do_main = True

while do_main:

	# moving the paddles
	pressed = pygame.key.get_pressed()

	pygame.key.set_repeat()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			do_main = False

	if pressed[pygame.K_ESCAPE]:
		do_main = False

	if pressed[pygame.K_w]:
		paddle1.moveDown()
	elif pressed[pygame.K_s]:
		paddle1.moveUp()

	if pressed[pygame.K_UP]:
		paddle2.moveDown()
	elif pressed[pygame.K_DOWN]:
		paddle2.moveUp()


	# collision of paddle with top/bottom of screen
	paddle1.updateVerticalPosition()

	paddle2.updateVerticalPosition()

	game_screen.fill(COURT_COLOR)


	for ball_id in ball_dict:

		ball = ball_dict[ball_id]

		ball.updatePosition()

		# left paddle
		if ball.getXPos() < paddle1.getXPos() + paddle1.getWidth() and ball.getYPos() >= paddle1.getYPos() and ball.getYPos() <= paddle1.getYPos() + paddle1.getHeight():
			ball.changeXVel()

		# right paddle
		if ball.getXPos() > paddle2.getXPos() and ball.getYPos() >= paddle2.getYPos() and ball.getYPos() <= paddle2.getYPos() + paddle2.getHeight():
			ball.changeXVel()

		# keeping score
		if ball.getXPos() <= 0:

			score_keeper.incrementPlayer2Score()
			
			remove_ball(ball_id)

			point_scored()

		elif ball.getXPos() >= screen_width:

			score_keeper.incrementPlayer1Score()

			remove_ball(ball_id)

			point_scored()

		ballr = pygame.draw.circle(game_screen, BALL_COLOR, (ball.getXPos(), ball.getYPos()), ball.getRadius(), 0)
		print("moving ball %s" % ball.getId())


	paddle_1 = pygame.draw.rect(game_screen, PADDLE_COLOR, (paddle1.getXPos(), paddle1.getYPos(), paddle1.getWidth(), paddle1.getHeight()), 0)
	
	paddle_2 = pygame.draw.rect(game_screen, PADDLE_COLOR, (paddle2.getXPos(), paddle2.getYPos(), paddle2.getWidth(), paddle2.getHeight()), 0)
	
	net = pygame.draw.line(game_screen, NET_COLOR, (screen_width/2,5), (screen_width/2, screen_height))
	
	score_text = font.render(str(score_keeper.getPlayer1Score()) + " " + str(score_keeper.getPlayer2Score()), 1, SCORE_TEXT_COLOR)

	game_screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, 10))

	pygame.display.update()

	time.sleep(0.016666667)



pygame.quit()

