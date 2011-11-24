#!/usr/bin/env python

# Single best explanation: http://is.gd/cUxhMv (SPOILER ALERT!)

import sys
import math
import tools.window as window

# fractal parameters
S = "AABAB"
X = (xmin, xmax) = (2.0, 4.0)
Y = (ymin, ymax) = (2.0, 4.0)

# default window size
# height set automatically
window_width = 200

# accuracy
limes_precision = 0.05
N_max = 10000

def sign( x ):
	return 1.0 if x>=0 else -1.0

def color( x ):
	if x > 0.75:
		return (255,255,255)
	if x > -1.0:
		c = int( ( x + 1.0 ) / 1.75 * 255 )
		return (255,c,c)
	if x > -4.0:
		c = int( ( x + 4.0 ) / 3.0 * 255 )
		return (c,0,0)
	else:
		return (0,0,0)

def r( n, a, b ):
	if S[n % len(S)] == 'A':
		return a
	else:
		return b

def L_exp( a, b ):
	x_n = 0.5
	sum = 0.0

	for n in xrange( 1, N_max+1 ):
		r_tmp = r( n, a, b )
		x_n = r_tmp * x_n * ( 1 - x_n )
		fa = math.fabs( r_tmp * ( 1 - 2*x_n ) )

		if fa > 0:
			diff = math.log( fa )
		else:
			diff = -40.0

		sum += diff
		if math.fabs( diff/n ) < limes_precision:
			break

	return sum/n


win = window.Window( window_width, 1.0, xmin, xmax, ymin )

n = 0
for (pixel, coord) in win.random():

	e = L_exp( *coord )
	win.plot( pixel, color(e) )

	if n%50 == 0:
		if win.quit():
			sys.exit( 0 )

	if pixel[0] == window_width - 1:
		win.update()

	#if n % 200 == 0:
	#	win.update()
	n += 1

win.update()
print "Done"

while 1:
	if win.quit():
		break

