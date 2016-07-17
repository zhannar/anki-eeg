import pandas as pd
import numpy as np

words = pd.read_csv("word_list.csv")
n = len(words)
print "total words:" , n

words_240 = np.random.choice(words["id"],size=240, replace=False)
words_120 = np.random.choice(words_240,size=120, replace=False)

final = words[words["id"].isin(words_240)].copy()
final["is_shown"] = 0

ids = list(final["id"])
is_shown = list(final["is_shown"])

for x in range(0,239):   
    if ids[x] in words_120:
        is_shown[x] = 1

final["is_shown"] = is_shown

print final