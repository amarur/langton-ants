# An implementation of Langston's Ant
# Built off of the abm-ants.py file in PyCX
# Anant Marur / amarur / 19237018
# CMPLXSYS 530, Lynette Shaw
# February 20, 2018

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 100 #toggle value
height = 100 #toggle value
populationSize = 40 #toggle value
proportionTrueLangtons = 0.5 #toggle value

white = 0 
black = 100

class Ant:
	#A read write, quad-directional agent
	#directionality is represented as an integer in [0,3], represented as follows:
	#		0
	#	1		3
	#		2
	def __init__(self, direction, xcoor, ycoor, breed):
		self.__direction = direction
		self.__xcoor = xcoor
		self.__ycoor = ycoor
		self.__breed = breed

	def step(self):
		global envir
		if (envir[self.__ycoor, self.__xcoor] == white) :
			if(self.__breed == 'r'):
				self.turnLeft()
			else:
				self.turnRight()
			envir[self.__ycoor, self.__xcoor] = black
			self.moveForward()
		else:
			if(self.__breed == 'r'):
				self.turnRight()
			else:
				self.turnLeft()
			envir[self.__ycoor, self.__xcoor] = white
			self.moveForward()



	def turnRight(self):
		self.__direction = (self.__direction - 1) % 4
	


	def turnLeft(self):
		self.__direction = (self.__direction + 1) % 4

	
	def moveForward(self):
		if(self.__direction == 0):
			self.__ycoor = (self.__ycoor + 1) % height
		elif (self.__direction == 1):
			self.__xcoor = (self.__xcoor - 1) % width
		elif (self.__direction == 2):
			self.__ycoor = (self.__ycoor - 1) % height
		else:
			self.__xcoor = (self.__xcoor + 1) % width

	def getX(self):
		return self.__xcoor
	
	def getY(self):
		return self.__ycoor

	def getBreed(self):
		return self.__breed


def init():
    global time, agents, envir

    time = 0

    agents = []
    for i in xrange(populationSize):
		breed = 'b'

		if (RD.random() <= proportionTrueLangtons) :
			breed = 'r'

		newAgent = Ant(RD.randint(0,3), RD.randint(0, width - 1), RD.randint(0, height - 1), breed)
		agents.append(newAgent)

    envir = SP.zeros([height, width])


def draw():
    PL.cla() #check 
    PL.pcolor(envir, cmap = PL.cm.binary)
    PL.axis('image')
    PL.hold(True)
    x = [ag.getX() + 0.5 for ag in agents]
    y = [ag.getY() + 0.5 for ag in agents]
    b = [ag.getBreed() for ag in agents]
    PL.scatter(x, y, c = b)
    PL.hold(False)
    PL.title('t = ' + str(time))


def step():
	global time, agents, envir

	time += 1

	for ag in agents:
		ag.step()

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])