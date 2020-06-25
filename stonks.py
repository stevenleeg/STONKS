#!/usr/bin/env python
import os
import time
try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen
import subprocess

prev_counter = None
current_counter = None
script_directory = os.path.dirname(os.path.abspath(__file__))

def play_sound():
    subprocess.run(['osascript', '-e', 'set Volume 10'])
    subprocess.run(['afplay', os.path.join(script_directory, 'STONKS.mp3')])

while True:
    try:
        response = urlopen('https://stevegattuso.me/stonks.txt').read()
        prev_counter = current_counter
        current_counter = int(response)

        # Don't play if we're fetching for the first time
        if prev_counter is None or current_counter is None:
            print('No counter, skipping')
        elif current_counter > prev_counter:
            print('New counter (%d)! STONKS!!!!!!' % current_counter)
            play_sound()
        else:
            print('Counter is still %d' % current_counter)
    except Exception as e:
        print('Could not make request, aborting: %s' % e)

    time.sleep(60)
