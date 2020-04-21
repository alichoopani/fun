from random import randint
import math
from time import sleep
import os


def make_universe(w, h):
	universe = [[0 for x in range(w)] for y in range(h)]
	for y in range(w):
		for x in range(h):
			if randint(1, 10) < 3 :
				universe[x][y] = 1
			else :
				universe[x][y] = 0
	return universe;
	
def print_universe(universe):
	for x in range(len(universe)):
		for y in range(len(universe[0])):
			if universe[x][y] == 0:
				print(' - ', end = '')
			else :
				print(' + ', end = '')
		print('\n')

def evolution(universe):
	h = len(universe)
	w = len(universe[0])
	new_universe = make_universe(w, h)

	for y in range(h):
		for x in range(w):
			lives = 0

			for i in range(9):
				mh = (y - 1) + math.floor(i / 3)
				mw = (x - 1) + i % 3
				if 0 <= (y - 1) + math.floor(i / 3) < h and 0 <= (x - 1) + i % 3 < w :
					#print(universe[mh][mw], end = '')
					if universe[mh][mw] == 1:
						lives += 1
			if universe[y][x] == 1:
				lives -= 1
				
			if lives == 3:
				new_universe[y][x] = 1
			elif universe[y][x] == 1 and lives == 2:
				new_universe[y][x] = 1
			else :
				new_universe[y][x] = 0

	return new_universe

def world():
	fake_world_question = input('do you want fake world?(y/n)\n')
	if fake_world_question == 'y':
		n = input('please inser your fake world code(between 1 to 4)\n')
		universe = make_fake_universe(int(n))
	else:
		w = input('please insert width of your world:')
		h = input('please insert height of your world:')
		universe = make_universe(int(w), int(h))
	
	while 1:
		os.system('clear')
		print_universe(universe)
		universe = evolution(universe)
		sleep(1)
		
def make_fake_universe(n):
	if n == 1:
		return [[0,0,0], [1,1,1], [0,0,0]]
	elif n == 2:
		return [[1,1,0,0], [1,1,0,0], [0,0,1,1], [0,0,1,1]]
	elif n == 3:
		return [[0,0,0,0,0], [0,0,1,1,1,0], [0,1,1,1,0,0], [0,0,0,0,0]]

world()
