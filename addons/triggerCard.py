import time

from anki.hooks import wrap
from aqt.reviewer import Reviewer

# showInfo to show dialog box. Not needed for actual trigger
from aqt.utils import showInfo

def triggerCard(self):
    # Triggers when 'nextCard' is called. 
    # Called when 'popping' card of queue.

    # show a message box with timestamp
    showInfo("Time Stamp: %s" % time.time())
    # TODO: Implement actuall callback when nextCard called

Reviewer.nextCard = wrap(Reviewer.nextCard, triggerCard)


