# evolve the population of compositions, creating new generations from selection, breeding, and mutation

import population
import genome

def evolve(mutation_rate, scale, total_population, generations):
    # executes the genetic algorithm until the total number of generations has been reached

    current_generation = population.Population(population_size=total_population, melodic_scale=scale)

    next_generation_compositions = []
    for i in range(generations):

        fitness_sum = 0
        # get the average fitness of the generation
        for composition in current_generation.compositions:
            fitness_sum += composition['fitness']

        # prints the fittest composition and the average fitness score for the current generation
        print ("Generation:", i, "Fittest:", current_generation.compositions[0]['fitness'], "AverageFitness:", fitness_sum / len(current_generation.compositions))
        # create next generation of compositions starting with the two fittest from the previous generation
        next_generation_compositions = current_generation.compositions[0:2]

        # adds to the next generation of compositions by selecting parents, crossing over their genes, and mutating the children
        for j in range(int(len(current_generation.compositions) / 2) - 1):
            child_A, child_B = genome.Genome.cross_over_breeding(current_generation.select_parents())
            # mutates the children
            child_A.mutate(mutation_rate)
            child_B.mutate(mutation_rate)
            # adds the two children from the crossover to the next generation
            next_generation_compositions += [{'genome': child_A}, {'genome': child_B}]

        # updates the population with the next generation of compositions
        current_generation.compositions = next_generation_compositions
        # updates the fitness scores array based on the new compositions
        current_generation.get_fitness_scores()
        # sorts the compositions in the population by their fitness score
        current_generation.sort_by_fitness()

    return current_generation
