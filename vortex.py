import os
from time import sleep

def make_vortex(w, h):
	vortex = [[0 for x in range(w)] for y in range(h)]
	for y in range(h):
		for x in range(w):
			vortex[y][x] = 0
	vortex[0][0] = 1	
	return vortex;
	
def print_vortex(vortex):
	for y in range(len(vortex)):
		for x in range(len(vortex[0])):
			if vortex[y][x] > 0:
				print(' + ', end='')
			else:
				print(' - ', end='')
		print('\n')

def get_last(vortex):
	maxx = 0
	maxy = 0
	max = 0
	for y in range(len(vortex)):
		for x in range(len(vortex[0])):
			if vortex[y][x] > max :
				max = vortex[y][x]
				maxx = x
				maxy = y
	return maxx, maxy 

def move(vortex, x, y, dir):
	ndir = dir
	nvortex = vortex
	if dir == 1:
		if x < len(vortex[0]) - 1 and vortex[y][x + 1] == 0:
			nvortex[y][x + 1] = vortex[y][x] + 1
		else:
			nvortex, ndir = move(vortex, x, y, 2)
	elif dir == 2:
		if y < len(vortex) - 1 and vortex[y + 1][x] == 0:
			nvortex[y + 1][x] = vortex[y][x] + 1
		else:
			nvortex, ndir = move(vortex, x, y, 3)
	elif dir == 3:		
		if x > 0 and vortex[y][x - 1] == 0:
			nvortex[y][x - 1] = vortex[y][x] + 1
		else:
			nvortex, ndir = move(vortex, x, y, 4)
	elif dir == 4:
		if y > 0 and vortex[y - 1][x] == 0:
			nvortex[y - 1][x] = vortex[y][x] + 1
		else:
			nvortex, ndir = move(vortex, x, y, 1)
	return nvortex, ndir 

def has_free(vortex):
	res = 0
	for y in range(len(vortex)):
		for x in range(len(vortex[0])):
			if vortex[y][x] == 0:
				res = 1
	return res

def game():
	w = int(input('please insert width of your world(int):'))
	h = int(input('please insert height of your world(int):'))
	vortex = make_vortex(w, h)
	print(w, h)
	dir = 1
	for j in range(w * h):
		os.system('clear')
		if has_free(vortex) == 1:
			x, y = get_last(vortex)
			print_vortex(vortex)
			vortex, dir = move(vortex, x, y, dir)
			sleep(1/20)
	print_vortex(vortex)

game()
