import pygame
from pygame.locals import *
from constants import *
import time
from csv_collector import CSVCollector
from extract_words import get_words
import pandas as pd

pygame.init()
pygame.mouse.set_visible(False)

from screen import screen
from drawstuff import *

study_time = int(time.time())
print(study_time)

eeg_fname='../data/eeg_{}.csv'.format(study_time)
word_fname = '../data/words_{}.csv'.format(study_time)

words = get_words()
words.to_csv(word_fname)

# collector = CSVCollector(port='/dev/ttyUSB0', fname=eeg_fname)

# collector.start()
# collector.tag(0)
# time.sleep(2)


def check_for_escape():
    while True:
        event = pygame.event.poll()
        if event.type == 0:
            return False
        elif event.dict.get('key', -1) == K_ESCAPE:
            return True

def finish_stuff(early=False):
    return

for i in xrange(words.shape[0]):
    d = dict(words.ix[i])

    word = d['word']

    simple_slide(word)
    # collector.tag(word)
    time.sleep(2)

    if check_for_escape():
        finish_stuff(early=True)
        # collector.stop()
        exit()

    focus_slide()
    # collector.tag('focus')
    time.sleep(0.5)

    if check_for_escape():
        finish_stuff(early=True)
        # collector.stop()
        exit()
