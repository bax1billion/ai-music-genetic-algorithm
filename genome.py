# encode the genome of a single individual composition (a sequence of notes)

import random
import copy

from settings import *

class Genome():
    # TODO: implement the init method to initialize the genome with a new data structure
    # the init method is currently unused
    def __init__(self, scale):
        self.scale = scale
        self.genome = []
        for x in range(8):
            self.genome.append(Bar(scale=self.scale, start_time=x * 4))
            
        # print the genome to the console for debugging
        # print("\n GENOME:", self.genome, "\n scale =", self.scale)
        # for bar in self.genome:
        #     print("\n BAR:", bar.notes, "\n start_time =", bar.start_time, "\n scale =", bar.scale, "\n note_groups =", bar.note_groups, "\n")
        #     for note in bar.notes:
        #         print("NOTE:", "pitch =", note.pitch, "time =", note.time, "duration =", note.duration, "volume =", note.volume)

        # TODO: include a time signature in the genome
     
    def mutate(self, rate):
        # mutates a sequence according to the mutation rate, 0.05 is a 10% total chance of any mutation (5% chance of each type of mutation)

        for i, bar in enumerate(self.genome):

            # TODO: get the new bar generation working
            # generate a new bar (mutation rate of 0.05 is a 5% chance)
            # new_bar = Bar(scale=bar.scale, start_time=bar.start_time)
            # self.genome[i] = new_bar
            # if random.uniform(0,1) <= rate:
            #     bar.mutate()

            for note in bar.notes:

                # mutate each note pitch and volume to a note from the scale or a rest at a random volume (mutation rate of 0.05 is a 5% chance)
                if random.uniform(0,1) <= rate:
                    note.mutate()

            # TODO: replace a bar with duplicated bar from the genome (mutation rate of 0.05 is a 5% chance)
            # this should add repeating patterns to the composition
            # if random.uniform(0,1) <= rate:
            #     bar_copy = copy.deepcopy(random.choice(self.genome))
            #     bar_copy.start_time = self.genome[i].start_time
            #     note_durations_sum = 0
            #     for note in bar.notes:
            #         note.time = bar_copy.start_time + note_durations_sum
            #         note_durations_sum += note.duration
            #     self.genome[i] = bar_copy

        # TODO: shuffle the bars in the genome (need to account for start time of each bar and notes)
        # %5 chance of randomly reordering the bars in the genome
        # if random.uniform(0,1) <= rate:
        #     genome = copy.deepcopy(random.shuffle(genome))
    
    @staticmethod
    def cross_over_breeding(parents):
        # performs a single point crossover of two parent sequences

        # select a bar position in the sequence as the single point of crossover
        cross_over_location = random.randint(1, len(parents[0]) - 1)

        genome_A = copy.deepcopy(parents[0]['genome'])
        genome_B = copy.deepcopy(parents[1]['genome'])

        # create offspring by combining the two parents at the crossover point
        cross_over_A = genome_A.genome[:cross_over_location] + genome_B.genome[cross_over_location:]
        cross_over_B = genome_B.genome[:cross_over_location] + genome_A.genome[cross_over_location:]

        genome_A.genome = cross_over_A
        genome_B.genome = cross_over_B

        return genome_A, genome_B

# the code below is still unused for now
# TODO: add a class for notes that includes pitch, duration, volume
class Note():
    def __init__(self, scale, duration, time, volume, group):
        self.scale = scale
        # a note value of None represents a rest
        self.pitch = random.choice(scale + [None])
        self.time = time
        self.duration = duration
        self.volume = volume
        self.group = group
    
    def mutate(self):
        # change the pitch and volume of a note
        self.pitch = random.choice(self.scale + [None])
        self.volume = random.randrange(1, 128)


# TODO: add a class for bars that includes a list of notes and a time signature
class Bar():
    # TODO: consider adding a time signature to the bar
    def __init__(self, scale, start_time):
        self.scale = scale
        self.start_time = start_time
        self.notes = []
        self.add_notes()
        #self.time_signature = time_signature
    
    def add_notes(self):
        # 4/4 time signature is 4 beats per bar, each beat is a quarter note
        # quarter note = duration is 1.0 in MIDI beats
        note_durations_sum = 0
        current_note_group = 0
        while note_durations_sum < 4:
            # use random duration from a list of durations
            duration = random.choice(note_durations)

            # ensure the bar doesn't exceed 4 beats
            if note_durations_sum + duration > 4:
                # TODO: instead ensure each note is one of the durations in the list from settings.py
                duration = 4 - note_durations_sum

            # set the random volume for the notes
            note_volume = random.randrange(1, 128)

            # number of simultaneous notes at the same time (put no more than five notes in a chord)
            total_concurrent_notes = random.randrange(1, 6)

            # create notes with a random pitches from the scale, a random duration, and a random volume
            for x in range(total_concurrent_notes):
                note = Note(scale=self.scale, duration=duration, time=(self.start_time + note_durations_sum), volume=note_volume, group=current_note_group)
                if total_concurrent_notes > 1:
                    # no need to insert a rest into a chord
                    if note.pitch is not None:
                        self.notes.append(note)
                # always append when note group is a single note
                else:
                    self.notes.append(note)

            note_durations_sum += note.duration
            current_note_group += 1

        # number of note groups in the bar
        self.note_groups = current_note_group
            
    # this class method is not currently in use
    def mutate(self):
        # regenerate the bar with new notes
        self.notes = []
        self.add_notes()
