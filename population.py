# create a population of individual musical compositions/genomes (each individual is a sequence of notes)

import random
import genome

from fitness import fitness_function

class Population:
    # generates multiple sequences of notes (genomes), which comprise the population of compositions
    def __init__(self, population_size, melodic_scale):
        self.melodic_scale = melodic_scale
        self.compositions = []
        for x in range(population_size):
            composition = genome.Genome(melodic_scale)
            fitness = fitness_function(composition.genome)
            self.compositions.append({'genome': composition, 'fitness': fitness})    
        self.sort_by_fitness()

    # sorts the population by fitness score
    def sort_by_fitness(self):
        self.compositions = sorted(self.compositions, key=lambda composition: composition['fitness'], reverse=True)
        return self.compositions
    
    # adds or updates the fitness scores for the compositions/genomes in the population
    def get_fitness_scores(self):
        for composition in self.compositions:
            composition['fitness'] = fitness_function(composition['genome'].genome)
        return self.compositions
    
    # selects two parents from the population to be used in crossover (probability of being selected is weighted by the fitness score of each sequence)
    def select_parents(self):
        weights_list = [composition['fitness'] for composition in self.compositions]
        parent_A, parent_B = random.choices(self.compositions, weights=weights_list, k=2)
        return parent_A, parent_B
