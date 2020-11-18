#!/usr/bin/env python
#coding=utf-8
#
#*	MyPi-SenseHat-PixelArt-random
#*	https://github.com/framboise-pi/MyPi-SenseHat-pixelart-random
#*	Copyright(C) 2020 Cedric Camille Lafontaine http://www.framboise-pi.fr,
#*	version 0.0.1
#

from sense_hat import SenseHat
import random
import time

sense = SenseHat()
sense.rotation = 270
sense.low_light = True
sense.clear()

print("...starting SenseHat random Pixel Art script...")

def ColorRandom():
	ra = random.randint(0,255)
	rb = random.randint(0,255)
	rc = random.randint(0,255)
	randomed = [ra,rb,rc]
	return randomed

def MakeRandomPixelArtV():
	array_pixel = []
	#pour fabriquer toutes les colonnes
	for i in range (0,8):
	#une ligne avec mirroir vertical - code a simplifier...
		one = ColorRandom()
		two = ColorRandom()
		three = ColorRandom()
		four = ColorRandom()
		array_pixel.append(one)
		array_pixel.append(two)
		array_pixel.append(three)
		array_pixel.append(four)
		array_pixel.append(four)
		array_pixel.append(three)
		array_pixel.append(two)
		array_pixel.append(one)
	sense.set_pixels(array_pixel)
	
while True:
	MakeRandomPixelArtV()
	time.sleep(5)
