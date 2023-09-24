# contains settings/configuration/data for the genetic algorithm

# number of individuals in the population
population_size = 1000
# number of generations to evolve the population
total_generations = 2000
# mutation rate (0.05 is 5% chance for each type of mutation)
mutation_rate = 0.05

# Wikipedia list of scales: https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes
# below dictionary represetns the semitones from the root note and the next note in the scale, the multiplier is for two octaves
# (each scale structure should add up to 12 before the multiplier)
scale_patterns = {
    "major": [2, 2, 1, 2, 2, 2, 1] * 7,
    "minor": [2, 1, 2, 2, 1, 2, 2] * 7,
    "major pentatonic": [2, 2, 3, 2, 3] * 7, # exaple integer notation of scale: (0,2,4,7,9)
    "minor pentatonic": [3, 2, 2, 3, 2] * 7,
    # inlcude the chromatic scale
    # "chromatic": [1] * 24,
    "blues": [3, 2, 1, 1, 3, 2] * 7, # example integer notation of scale: (0,3,5,6,7,10)
    "phrygian": [1, 2, 2, 2, 1, 2, 2] * 7, # example integer notation of scale: (0,1,3,5,7,8,10)
    "hungarian": [2, 1, 3, 1, 1, 3, 1] * 7, # example integer notation of scale: (0,2,3,6,7,8,11)
}

# 88-key piano has seven octaves plus three lower notes (A, B, and B flat) below the bottom C. The top C is the 88th key on the piano keyboard.
# 88 key is considered a full sized piano
# 7 octaves, treble clef: (C4 is one ledger line below staff) bass clef: (C4 is one ledger line above staff)
key_codes = {
    "a":  21,
    "a#": 22,
    "bb": 22, # alias for "a#
    "b":  23,
    "c":  24,
    "c#": 25,
    "db": 25, # alias for "c#"
    "d":  26,
    "d#": 27,
    "eb": 27, # alias for "d#"
    "e":  28,
    "f":  29,
    "f#": 30,
    "gb": 30, # alias for "f#"
    "g":  31,
    "g#": 32,
}

# MIDI codes 21 to 108 represent the full range of an 88 key piano
# dictionary containing the MIDI code for every note of an 88 key piano
# the dictionary below is only used for reference, the MIDI codes are not used in the program
midi_note_codes = {
    "a0": 21,
    "a#0": 22,
    "bb0": 22, # alias for "a#
    "b0": 23,
    "c1": 24,
    "c#1": 25,
    "db1": 25, # alias for "c#"
    "d1": 26,
    "d#1": 27,
    "eb1": 27, # alias for "d#"
    "e1": 28,
    "f1": 29,
    "f#1": 30,
    "gb1": 30, # alias for "f#"
    "g1": 31,
    "g#1": 32,
    "ab1": 32, # alias for "g#"
    "a1": 33,
    "a#1": 34,
    "bb1": 34, # alias for "a#"
    "b1": 35,
    "c2": 36,
    "c#2": 37,
    "db2": 37, # alias for "c#"
    "d2": 38,
    "d#2": 39,
    "eb2": 39, # alias for "d#"
    "e2": 40,
    "f2": 41,
    "f#2": 42,
    "gb2": 42, # alias for "f#"
    "g2": 43,
    "g#2": 44,
    "ab2": 44, # alias for "g#"
    "a2": 45,
    "a#2": 46,
    "bb2": 46, # alias for "a#"
    "b2": 47,
    "c3": 48,
    "c#3": 49,
    "db3": 49, # alias for "c#"
    "d3": 50,
    "d#3": 51,
    "eb3": 51, # alias for "d#"
    "e3": 52,
    "f3": 53,
    "f#3": 54,
    "gb3": 54, # alias for "f#"
    "g3": 55,
    "g#3": 56,
    "ab3": 56, # alias for "g#"
    "a3": 57,
    "a#3": 58,
    "bb3": 58, # alias for "a#"
    "b3": 59,
    "c4": 60,
    "c#4": 61,
    "db4": 61, # alias for "c#"
    "d4": 62,
    "d#4": 63,
    "eb4": 63, # alias for "d#"
    "e4": 64,
    "f4": 65,
    "f#4": 66,
    "gb4": 66, # alias for "f#"
    "g4": 67,
    "g#4": 68,
    "ab4": 68, # alias for "g#"
    "a4": 69,
    "a#4": 70,
    "bb4": 70, # alias for "a#"
    "b4": 71,
    "c5": 72,
    "c#5": 73,
    "db5": 73, # alias for "c#"
    "d5": 74,
    "d#5": 75,
    "eb5": 75, # alias for "d#"
    "e5": 76,
    "f5": 77,
    "f#5": 78,
    "gb5": 78, # alias for "f#"
    "g5": 79,
    "g#5": 80,
    "ab5": 80, # alias for "g#"
    "a5": 81,
    "a#5": 82,
    "bb5": 82, # alias for "a#"
    "b5": 83,
    "c6": 84,
    "c#6": 85,
    "db6": 85, # alias for "c#"
    "d6": 86,
    "d#6": 87,
    "eb6": 87, # alias for "d#"
    "e6": 88,
    "f6": 89,
    "f#6": 90,
    "gb6": 90, # alias for "f#"
    "g6": 91,
    "g#6": 92,
    "ab6": 92, # alias for "g#"
    "a6": 93,
    "a#6": 94,
    "bb6": 94, # alias for "a#"
    "b6": 95,
    "c7": 96,
    "c#7": 97,
    "db7": 97, # alias for "c#"
    "d7": 98,
    "d#7": 99,
    "eb7": 99, # alias for "d#"
    "e7": 100,
    "f7": 101,
    "f#7": 102,
    "gb7": 102, # alias for "f#"
    "g7": 103,
    "g#7": 104,
    "ab7": 104, # alias for "g#"
    "a7": 105,
    "a#7": 106,
    "bb7": 106, # alias for "a#"
    "b7": 107,
    "c8": 108
}

# helpful resources:
# https://en.wikipedia.org/wiki/Semitone
# https://en.wikipedia.org/wiki/Harmonic_series_(music)
# https://en.wikipedia.org/wiki/Interval_(music)
# https://www.musiccrashcourses.com/lessons/harmony.html

# this dictionary assigns different values to different intervals (in semitones)
interval_weights = {
    0 : 10,    # unison (repeated note) - consonant
    1 : -10,   # minor second - dissonant
    2 : -5,   # major second - somewhat dissonant
    3 : 5,    # minor third - somewhat consonant
    4 : 5,    # major third - somewhat consonant
    5 : 10,    # perfect fourth - consonant
    6 : -10,   # tritone - dissonant
    7 : 10,    # perfect fifth - consonant
    8 : 5,    # minor sixth - somewhat consonant
    9 : 5,    # major sixth - somewhat consonant
    10 : -5,  # minor seventh - somewhat dissonant
    11 : -10,  # major seventh - dissonant
    12 : 10,   # octave - consonant
}

# TODO: consider adding duration into the genome
# MIDI beats (float for quarter notes)
# https://midiutil.readthedocs.io/en/1.2.1/common.html#adding-notes
note_durations = [
    0.0625,     # sixty-fourth note
    0.09375,    # dotted sixty-fourth note
    0.125,      # thirty-second note
    0.1875,     # dotted thirty-second note
    0.25,       # sixteenth note
    0.375,      # dotted sixteenth note
    0.5,        # eighth note
    0.75,       # dotted eighth note
    1.0,        # quarter note
    1.5,        # dotted quarter note
    2.0,        # half note
    3.0,        # dotted half note
    4.0,        # whole note
    # TODO: consider adding longer notes when supporting multiple time signatures
    #6.0,       # dotted whole note
]
