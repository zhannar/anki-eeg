# anki-eeg

Using EEG recording, we train a classifier to predict the success of memory encoding of information. See [this post](http://lambdaloop.github.io/predicting-memory-encoding-using-openbci) for more details on setup and analysis.

Currently, we are using a random selection of words from the English Language. Extensions of this experiment can involve phone numbers, pictures, sound, and other stimuli.

The inspiration for this project was from the abstract: [Improving Memory Performance Using a Wearable BCI](http://doi.org/10.3217/978-3-85125-467-9-128) presented at the [2016 International BCI Society Meeting](http://bcisociety.org/meetings/bci-meeting-2016-abstracts-2/). Our hopes are to first replicate this study, and then apply the processing and analytic pipeline for easy integration with Anki.

[Anki](http://ankisrs.net/) is a flashcard application that is opensource. It was developed in a way to allow for easy creation of 'addons' to extend the base app. The addon we are building will trigger a timestamp event to the EEG datastream for epoching data used for building the classifer.

Word list and word features was randomly  generated from the [Paivio et al. Word List Generator](http://www.datavis.ca/online/paivio/).



### Experimental Procedure Outline

-   Attach OpenBCI to participant's head.
-   Record positions of EEG according to 10-20 system.
-   Have participant sit in chair in front of monitor
-   Run OpenBCI processing sketch to 'test' connections
-   Present list of words. (`encode.py`)
-   Wait 4-5 minutes before recall test (Listen to Rite of Spring or other way to kill the time)
-   Start Recall Procedure `recognize.py`

### How to Run

#### Stimulus Presentation + Recording
- `cd paradigm` 
- Run `python encode.py`
- This will start the csv collection (watch out for hardcoded usb paths inside `encode.py`) 
- This will start the Pygame presentation of the words while recording data in csv file in `data` directory

#### Recall
- `cd paradigm`
- `python recognize.py`



### More Info on [Improving Memory Performance Using a Wearable BCI](http://doi.org/10.3217/978-3-85125-467-9-128): 

```
Corroborating previous studies [1,2,3], averaging over multiple EEG trials of the
encoding phase suggest that the power of the pre-stimulus theta and beta and the power of alpha after the onset of
the words over the parietal/occipital electrodes could be potentially useful as features for identifying poorly
versus well encoded words. Moreover, signal amplitudes from 1.5 to 2s after the onset of the words in the
parietal/occipital electrodes were significantly different between the two conditions 
```
[1](http://www.sciencedirect.com/science/article/pii/S1053811915010460) Schneider SL, Rose M. Intention to encode boosts memory-related pre-stimulus EEG beta power. NeuroImage. 125: 978-87, 2016.

[2](https://www.researchgate.net/profile/Simon_Hanslmayr/publication/239071542_How_brain_oscillations_form_memories_-_a_processing_based_perspective_on_oscillatory_subsequent_memory_effects/links/00b495285a483db58d000000.pdf) Hanslmayr S, Staudigl T. How brain oscillations form memories-a processing based perspective on oscillatory subsequent memory
effects. Neuroimage. 85:648-55, 2014.

[3](http://www.weizmann.ac.il/neurobiology/labs/dudai/uploads/files/Cohen_et_al_2014.pdf) Cohen N, Pell L, Edelson MG, Ben-Yakov A, Pine A, Dudai Y. Peri-encoding predictors of memory encoding and consolidation.
Neuroscience & Biobehavioral Reviews. 50:128-42, 2015.
