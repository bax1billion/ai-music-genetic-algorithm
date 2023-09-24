# generate a midi file from a genome sequence of notes

import random

from midiutil import MIDIFile

from settings import *

class Midi:
    # outputs a midi file to disk, taking the genome sequence of notes and the file name as parameters
    def __init__(self, genome, file_name, tempo):
        self.genome = genome
        self.file_name = file_name
        self.tempo = tempo
        self.create_file()

    def create_file(self):
        # MIDIFile documentation: https://midiutil.readthedocs.io/en/1.2.1/common.html
        # channels are a set of tracks, possible to have multiple tracks in a channel (e.g. base and melody)

        time = 0
        track = 0
        channel = 0

        # one track
        midi_file = MIDIFile(1)
        midi_file.addTempo(track, time, self.tempo)

        for bar in self.genome.genome:
            for note in bar.notes:
                # print the notes to the console for debugging
                # print("NOTE:", "pitch:", note.pitch, "time:", note.time, "dur:", note.duration, "vol:", note.volume)
                # if pitch is "None", it's a rest
                if note.pitch is not None:
                    midi_file.addNote(track, channel, note.pitch, note.time, note.duration, note.volume)

                # time is incremented for duration of a rest (it's also the time between consecutive note strating times)
                time += note.duration

        # Save the MIDI file to disk
        with open(self.file_name, "wb") as f:
            midi_file.writeFile(f)
        with open("midi_files/latest.midi", "wb") as f:
            midi_file.writeFile(f)

