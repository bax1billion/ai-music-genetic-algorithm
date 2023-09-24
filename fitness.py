# evaluate the fitness of a given individual

from settings import *

# TODO: add more criteria to the fitness function
def fitness_function(genome):
    # calculates the fitness of a given sequence of notes (genome) based on smoothness and rhythm

    # TODO: consider adding a penalty for too many leaps in the same direction
    # TODO: consider adding a penalty for too many leaps in the same direction in the same bar

    # TODO: evaluate and promote patterns in the composition
    # TODO: promote longer note durations when they are at preffered intervals
    # TODO: promote louder notes when they are at preffered intervals

    # multiply the scores by their respective weights and sum them to get the fitness score
    harmony_weight = 4
    smoothness_weight = 3
    rhythm_weight = 1
    dynamic_weight = 1
    chord_weight = 5
    
    # initialize the fitness score variables to zero
    # harmonic is when notes are played at the same time, melodic is when notes are played sequentially
    harmonic_score = 0
    # smoothness measures the distance between sequential notes (conjunct/stepwise motion or disjunct/leaps)
    smoothness_score = 0
    # rhythm measures the number of rests in the composition
    rhythmic_score = 0
    # harmonic score for chords of simultaneous notes
    chord_score = 0
    # dynamic score for pitch range and volume of notes
    dynamic_score = 0

    # initialize the count variables to zero
    total_rests = 0
    total_notes = 0
    consecutive_rests = 0

    # highest and lowest notes
    highest_note = 0
    lowest_note = 109
    # TODO: score average pitch of the piece

    # loudest and quietest notes
    loudest_note = 0
    quietest_note = 128
    # TODO: score average volume of the piece

    # iterate through each bar in the composition
    for i, bar in enumerate(genome):
        
        # iterate through each note group in the bar and score the harmonic intervals for the chords
        for current_group in range(bar.note_groups):
            # get the notes in the current note group
            concurrent_note_pitches = [note.pitch for note in bar.notes if note.group == current_group and note.pitch is not None]
            # sort the notes in the chord by pitch 
            concurrent_note_pitches.sort()

            # promote consonant chords and demote dissonant chords
            for j, pitch in enumerate(concurrent_note_pitches):
                if j > 0:
                    # get the absolute interval differenece (in semitones) between the current note and the previous note
                    semitone_difference = abs(pitch - concurrent_note_pitches[j -1]) % 12
                    # sum the harony with the value of the semitone interval from the dictionary
                    chord_score += interval_weights[semitone_difference]

        for j, note in enumerate(bar.notes):
            # increment the total number of notes
            total_notes += 1

            # get total rests
            if note.pitch is None:
                total_rests += 1

            # get min and max notes
            if note.pitch is not None:
                if note.pitch > highest_note:
                    highest_note = note.pitch
                if note.pitch < lowest_note:
                    lowest_note = note.pitch
                if note.volume > loudest_note:
                    loudest_note = note.volume
                if note.volume < quietest_note:
                    quietest_note = note.volume
            
            # get total consecutive rests
            if i > 0 and j == 0 and note.pitch is None and genome[i - 1].notes[-1].pitch is None:
                consecutive_rests += 1
            elif j > 0 and note.pitch is None and genome[i].notes[j - 1].pitch is None:
                consecutive_rests += 1

            # smoothness can only be determined if not the first note of the copostion and preceding note not a rest and current note not a rest
            if note.pitch is not None and j == 0 and i > 0:
                # print("i", i)
                # print("genome[i - 1].notes", genome[i - 1].notes)
                # print("genome[i - 1]", genome[i - 1])
                if genome[i - 1].notes[-1].pitch is not None:
                    previous_note = genome[i - 1].notes[-1]
                
            elif note.pitch is not None and j > 0 and genome[i].notes[j - 1].pitch is not None:
                previous_note = genome[i].notes[j - 1]

                # get the absolute interval differenece (in semitones) between the current note and the previous note
                semitone_difference = abs(note.pitch - previous_note.pitch) % 12
                # sum the harony with the value of the semitone interval from the dictionary
                harmonic_score += interval_weights[semitone_difference]

                # smoothness is related to sequential interval changes in the melody
                # https://en.wikipedia.org/wiki/Melody
  
                # promote smaller intervals
                if semitone_difference <= 2:
                    smoothness_score += 10
                elif semitone_difference <= 4:
                    smoothness_score += 8
                elif semitone_difference <= 6:
                    smoothness_score += 6
                elif semitone_difference <= 8:
                    smoothness_score += 4
                elif semitone_difference <= 10:
                    smoothness_score -= 2
                elif semitone_difference <= 12:
                    smoothness_score -= 0
                else:
                    smoothness_score -= 10

    # promote sequences with less than 10% rests
    if total_rests * 10 <= total_notes:
        rhythmic_score += 10

    # promote sequences more dynamic range
    volume_range = loudest_note - quietest_note
    dynamic_score += volume_range

    # promote sequences more pitch range
    pitch_range = highest_note - lowest_note
    dynamic_score += pitch_range

    # apply penalty for occurrences of adjacent rests
    if consecutive_rests:
        rhythmic_score -= (consecutive_rests * 10)

    # TODO: improve the rythmic score by scoring the duration of the notes, repeating patterns, and syncopation

    #print("harmonic_score", harmonic_score, "smoothness_score", smoothness_score, "rhythmic_score", rhythmic_score, "dynamic_score", dynamic_score, "chord_score", chord_score)
    # multiply the scores by their respective weights and sum them to get the fitness score
    fitness = (harmonic_score * harmony_weight) + (smoothness_score * smoothness_weight) + (rhythmic_score * rhythm_weight) + (dynamic_score * dynamic_weight) + (chord_score * chord_weight)
    return fitness