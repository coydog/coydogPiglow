#!/usr/bin/python2
#
# Example script for coydgoPiglow module. Strobe all LED's individually in
# random sequence. usage:
# ./piglow-onepulse.py <brightness increment> <maximum time between LED's> <time increment>

import random
import time
import coydogPiglow
import sys

try:
	values = []
	i = 0
	while i < 18:
		values.append(0);
		i += 1
	bright = 255

	step_abs = 1
	if len(sys.argv) > 1:
		step_abs = int(sys.argv[1])
	if step_abs < 1:
		step_abs = 1

	sleep_max = 0
	if len(sys.argv) > 2:
		sleep_max = float(sys.argv[2])

	sleep_step = 0.001
	if len(sys.argv) > 3:
		sleep_step = float(sys.argv[3])

	sleep_curr = sleep_step
        while True:
		done = False
		step = step_abs
		i = random.randrange(0,18)
		while not done:
			values[i] += step
			coydogPiglow.update_leds(values)

			if values[i] >= bright:
				step = step * -1
			if step < 0  and values[i] <= 0:
				done = True;
			
		if sleep_max > 0:
			if sleep_curr >= sleep_max or (sleep_curr + sleep_step) <= 0:
				sleep_step *= -1
			sleep_curr += sleep_step
			print sleep_curr
		 	time.sleep(sleep_curr) #TODO: cycle through range

except KeyboardInterrupt:
	# set all the LEDs to "off" when Ctrl+C is pressed before exiting
	coydogPiglow.deInit()

