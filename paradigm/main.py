import pygame
from pygame.locals import *
from constants import *
import time
from csv_collector import CSVCollector

study_time = int(time.time())

fname='../data/eeg_data_{}.csv'.format(study_time)
collector = CSVCollector(port='/dev/ttyUSB0', fname=fname)

collector.start()
collector.tag(0)
time.sleep(2)

pygame.init()

from screen import screen
from drawstuff import *

from words import words


pygame.mouse.set_visible(False)

def check_for_escape():
    while True:
        event = pygame.event.poll()
        if event.type == 0:
            return False
        elif event.dict.get('key', -1) == K_ESCAPE:
            return True

def finish_stuff(early=False):
    return


for word in words:
    simple_slide(word)
    collector.tag(word)
    time.sleep(2)

    if check_for_escape():
        finish_stuff(early=True)
        collector.stop()
        exit()

    focus_slide()
    collector.tag('focus')
    time.sleep(0.5)

    if check_for_escape():
        finish_stuff(early=True)
        collector.stop()
        exit()
