# The codes in this file and some of the idea for the application flow was initially adapted from https://medium.com/dc-csr/how-i-made-a-genetic-algorithm-that-generates-music-67b90cd0d05e
# source code: https://github.com/taimurshaikh/MusicGeneticAlgorithm/tree/main

# genetic algorithm for music generation, accepts a user selected key and tempo to evolve a melodic musical composition

import time

# need this to play the MIDI file
import pygame

import scales
import midi

from settings import *
from evolution import evolve
#import player

# TODO: consider there is about 24 measures in a piano concerto per minute. If population with individuals of 8 bars, combine three individuals to get 24 bars (different tempos is ok, and represent movement in music)

# TODO: consider two bars for base, 8 bars for melody, and 4 bars for harmony (treble clef)

print("Welcome to the Genetic Algorithm Music Generator!")

def main():
    # entry point function of the genetic algorithm, also contains the user interface

    # get the time at the start of the program (used to calculate execution time)
    startTime = time.time()

    # print(midi_note_codes)
    # print(scale_patterns)

    # TODO: change this to use a random scale
    # display the scale options to the user
    print("Please select a scale:")
    def display_scales():
        for scale in [scale_name for scale_name in scale_patterns.keys()]:
            print(" ", scale)
    display_scales()

    selected_scale = input(" ").lower().strip()
    while selected_scale not in scale_patterns.keys():
        print("Please type the name of a scale to use from the list below (example: 'major'):")
        display_scales()
        selected_scale = input().lower().strip()

    # TODO: change this to use a random starting note
    starting_note = input("Please select a key (a, a#, bb, b, c, c#, etc.) ").lower().strip()
    while starting_note not in key_codes.keys():
        starting_note = input("Please type the note of the key (example: 'c' for key of C,'bb' for B Flat, or 'g#' for G Sharp): ").lower().strip()

    # create a list of MIDI note/pitch codes based on the selected scale and starting note
    scale = scales.Scale(starting_note, selected_scale)

    # TODO: support multiple time signatures
    # TODO: change this to use a random time signiture
    # time_signiture = input("Please enter a time signiture: ").strip()
    # while time_signiture not in time_signitures.keys():
    #     time_signiture = input("Please enter a time signiture (example: '4/4'): ").strip()

    # TODO: change this to use a random tempo
    selected_tempo = int(input("Please type a tempo between 30 and 300 *inclusive (BPM): ").strip())
    while not (selected_tempo >= 30 and selected_tempo <= 300):
        selected_tempo = int(input("Please type a tempo between 30 and 300 *inclusive (BPM) (example: '120'): ").strip())
    selected_tempo = int(selected_tempo)

    # run the genetic algorithm and get the resulting population
    result = evolve(mutation_rate, scale.scale, population_size, total_generations)

    # get the fitness score of the fittest individual
    fittest = result.compositions[0]['fitness']

    # export the MIDI file to disk
    midi.Midi(result.compositions[0]['genome'], f"midi_files/fit-{fittest}-gen{total_generations}-pop{population_size}.midi", selected_tempo)

    # get the time at the end of the program (used to calculate execution time)
    endTime = time.time()

    # print("genome: ", result.compositions[0]['genome'])
    print("EXECUTION TIME:", endTime - startTime)

    # write the execution time and fittest score to a log file
    with open("execution.log", 'a+') as f:
        f.write("fittest: " + str(fittest) + " generations: " + str(total_generations) + " population: " + str(population_size) + " time: " + str(endTime - startTime) + "\n" + "genome: " + str(result.compositions[0]['genome'].genome) + "\n" + "\n")

    # optionally play the MIDI file
    playMidi = input("Play the generated MIDI? choose y/n: ").strip()
    while not playMidi == "y" and not playMidi == "n":
        playMidi = input("Invalid. Choose y or n: ").strip()
    if playMidi == "y":
        exec(open('player.py').read())

if __name__ == "__main__":
    main()