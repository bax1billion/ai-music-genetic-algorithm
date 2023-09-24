# create list of MIDI pitch codes for a specifc musical key, using a starting note and a scale pattern

from settings import *

class Scale:
    # builds a scale based on the input values for root and key, and referencing the scale pattern and midi note dictionaries
    def __init__(self, root, key):
        self.root = root
        self.key = key
        self.make_scale()

    def make_scale(self):
        pattern = scale_patterns[self.key] # major, minor, etc.
        root_note_code = key_codes[self.root] # c4 is 60, etc.
        self.scale = [root_note_code] # initialize the scale with the root note
        
        current_note_code = root_note_code
        # creates the scale of note codes by appending integers summing the pattern values and begining from the root_note_code (see: scale_patterns dictionary in settings.py)
        for i, j in enumerate(pattern):
            current_note_code += j
            # only allow notes in the range of a full sized piano (88 keys)
            if current_note_code <= 108:
                self.scale.append(current_note_code) # add the next note in the scale
        return self.scale