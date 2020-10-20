import os
import time
import pygame
import game
import defaultvalues as df

def print_board(board):	
	for row in range(25):
		for column in range(25):
			color = df.WHITE
			if board[row][column] == 1:
				color = df.BLUE
			pygame.draw.rect(screen, color, [(df.MARGIN+df.WIDTH)*column+df.MARGIN,(df.MARGIN+df.HEIGHT)*row+df.MARGIN,df.WIDTH,df.HEIGHT])
			
	clock.tick(20)
	pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode(df.SIZE)
pygame.display.set_caption(df.TITLE)
clock = pygame.time.Clock()

geracao = game.estadoinicial()
print_board(geracao)
time.sleep(2)
done = False

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			geracao = game.estadoinicial()
			print_board(geracao)
			time.sleep(2)
    
	geracao = game.evolue(geracao)
	time.sleep(1)
	print_board(geracao)
	clock.tick(40)

