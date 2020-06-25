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
home_dir = os.path.expanduser('~')
stonks_dir = os.path.join(home_dir, '.stonks')

def play_sound():
    resp = subprocess.check_output(['osascript', '-e', 'output volume of (get volume settings)'])
    prev_volume = int(int(resp.decode('utf-8').replace('\n', '')) / 10)
    subprocess.call(['osascript', '-e', 'set Volume 10'])
    subprocess.call(['afplay', os.path.join(stonks_dir, 'STONKS.mp3')])
    subprocess.call(['osascript', '-e', 'set Volume %d' % prev_volume])

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
