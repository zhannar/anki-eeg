# anki-eeg
Using EEG data, we train a classifier to determine whether the brain is in a good or bad state for learning

The inspiration for this project was from the paper: [Improving Memory Performance Using a Wearable BCI](http://doi.org/10.3217/978-3-85125-467-9-128). 

Word list and word features was randomly  generated from the [Paivio et al. Word List Generator](http://www.datavis.ca/online/paivio/).

## How to Run

### Stimulus Presentation + Recording
- `cd paradigm` 
- Run `python encode.py`
- This will start the csv collection (watch out for hardcoded usb paths inside `encode.py`) 
- This will start the Pygame presentation of the words while recording data in csv file in `data` directory

### Recall
- `cd paradigm`
- `python recognize.py`

