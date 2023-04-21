"""Genetic algorithm for solving the N Queens Problem
Created by Brian Bemman based in part on pseudo-code provided in Russell and Norvig (2010).

Problem formulation:

Represent the complete state of the chessboard as an "individual" consisting of 8 queens -- one placed in each of the 
8 columns -- where a number indicates the row position on the chessboard. For example, [6, 3, 1, 8, 5, 2, 4, 7] 
denotes a queen in row 6 (from bottom) of the first column, a queen in row 3 of the second column, and so on.

A solution is an individual with a maximum fitness -- where no one of its queens is attacking (vertically, horizontally, 
diagonally) another on the chessboard -- specified by the fitness function.

initial state:              a configuration of 8 queens placed randomly by row for each of the 8 columns
actions:                    reproduce, mutate, selection
transition model:           two-parent-single-offspring reproduction with random crossover point; randomly selected 
                            single-gene mutation with randomly selected queen and position
goal test:                  whether or not an individual has a fitness equal to the maximum fitness level specified 
                            by a solution
path cost:                  N/A

"""

import random


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome  # state of the chessboard i.e., some configuration of 8 queens
        self.board = self.board
        self.fitness = self.fitness(chromosome)  # fitness equal to the number of non-attacking pairs of queens

    def initial_fitness(arr1, arr2):
        num_matching_tiles = 0
        for i, j in zip(arr1, arr2):
            if i == j:
                num_matching_tiles += 1
        return num_matching_tiles

    @staticmethod
    def fitness(chromosome, board):
        """O(n^2): Determines the fitness of an individual, defined as max_fitness minus the number of pairs of attacking queens.
            For example, the max_fitness is 28 non-attacking pairs of queens, so for an individual with 20 attacking pairs of queens,
            its fitness would be a rather low score of 28 – 20 = 8."""
        max_fitness = int(len(chromosome) * ((len(chromosome) - 1) / 2))
        for i in range(len(chromosome)):
            for j in range(i + 1, len(chromosome)):
                if chromosome[i] == chromosome[j]:  # horizontal
                    board += 1
                if (chromosome[i] + i) == (chromosome[j] + j):  # negative diagonal
                    board.num_matching_tiles += 1
                if (chromosome[i] - i) == (chromosome[j] - j):  # positive diagonal
                    board.num_matching_tiles += 1
        return max_fitness - board

    #@staticmethod
    #def fitness(chromosome):
    #    """O(n): Determines the fitness of an individual, defined as max_fitness minus the number of pairs of attacking queens.
    #            For example, the max_fitness is 28 non-attacking pairs of queens, so for an individual with 20 attacking pairs of queens,
    #            its fitness would be a rather low score of 28 – 20 = 8."""
    #    max_fitness = int(len(chromosome) * ((len(chromosome) - 1) / 2))
    #    horizontal = [0] * len(chromosome)
    #    negative_diagonal = [0] * 2 * len(chromosome)
    #    positive_diagonal = [0] * 2 * len(chromosome)
    #    num_attacking_pairs = 0
    #    for i in range(len(chromosome)):
    #        horizontal[chromosome[i] - 1] += 1
    #        negative_diagonal[chromosome[i] - 1 + i] += 1
    #        positive_diagonal[len(chromosome) - chromosome[i] + i] += 1
    #    for i in range(len(chromosome) * 2):
    #        if i < len(chromosome):
    #            num_attacking_pairs += (horizontal[i] * (horizontal[i] - 1)) / 2
    #        num_attacking_pairs += (negative_diagonal[i] * (negative_diagonal[i] - 1)) / 2
    #        num_attacking_pairs += (positive_diagonal[i] * (positive_diagonal[i] - 1)) / 2
    #    return int(max_fitness - num_attacking_pairs)


def fitness_proportionate_selection(population) -> Individual:
    """Selects a single parent according to fitness proportionate selection i.e., Roulette Wheel selection. A parent
    may be chosen more than once for a given population."""
    total_fitness = sum(individual.fitness for individual in population)
    threshold = random.uniform(0, total_fitness)
    running_sum = 0
    for individual in population:
        running_sum += individual.fitness
        if running_sum > threshold:
            return individual
    return population[0]  # fail safe returns the first individual


def reproduce(first_parent: Individual, second_parent: Individual) -> Individual:
    """Generates a single offspring of two parents from a random cross-over point."""
    crossover_point = random.randint(0, len(first_parent.chromosome) - 1)
    return Individual(first_parent.chromosome[0:crossover_point] + second_parent.chromosome[crossover_point:])


def mutate(offspring: Individual) -> Individual:
    """Mutates a single gene (i.e., number) of an offspring at a random location with a valid random number."""
    rand_idx = random.randint(0, len(offspring.chromosome) - 1)
    offspring.chromosome[rand_idx] = random.randint(1, len(offspring.chromosome))
    return Individual(offspring.chromosome)


def random_individual(num_of_queens) -> Individual:
    """Generates a random valid individual consisting of one row number [1, num_of_queens] for each column of the
    chessboard. """
    return Individual([random.randint(1, num_of_queens) for _ in range(num_of_queens)])


def random_population(num_of_queens, population_size) -> list():
    """Generates a random population of individuals."""
    return [random_individual(num_of_queens) for _ in range(population_size)]


def retrieve_most_fit(population) -> Individual:
    """Retrieves the most fit individual from a population of individuals."""
    most_fit_individual = population[0]
    for individual in population:
        if individual.fitness > most_fit_individual.fitness:
            most_fit_individual = individual
    return most_fit_individual


def print_most_fit(individual, generation_num) -> None:
    """Prints the maximally fit individual (i.e., solution) on an N x N chessboard of zeros."""
    board = [[0] * len(individual.chromosome) for _ in range(len(individual.chromosome))]
    print('Most fit configuration:')
    for idx, _ in enumerate(board):
        board[(len(individual.chromosome) - 1) - (individual.chromosome[idx] - 1)][idx] = 1
    for row in board:
        print(row)
    print('Individual:')
    print(individual.chromosome)
    print('Fitness:')
    print(individual.fitness)
    print('Number of generations:')
    print(generation_num)
    return None


def genetic_algorithm(population, max_fitness) -> (Individual, int):
    """Generates a population of individuals by two-parent-single-offspring reproduction. Parents have a probability of
        being selected for crossover proportional to their individual fitness when compared with the total overall fitness
        of the population. A single set of parents are selected for cross-over and their genes are joined via a random
        cross-over point to form a single offspring. Offspring have a positive but negligible probability of mutation where
        a single gene at a random location is randomly mutated."""
    mutation_probability = 0.05
    generation_num = 1
    while max_fitness not in [individual.fitness for individual in population] and generation_num < 1000:
        new_population = []
        for _ in range(len(population)):
            first_parent = fitness_proportionate_selection(population)
            second_parent = fitness_proportionate_selection(population)
            offspring = reproduce(first_parent, second_parent)
            if random.random() < mutation_probability:
                offspring = mutate(offspring)
            new_population.append(offspring)
        population = new_population
        generation_num += 1
    return retrieve_most_fit(population), generation_num


def main():
    #num_of_queens = 8
    #population_size = 100
    #max_fitness = int(num_of_queens * ((num_of_queens - 1) / 2))  # maximum fitness is 28 for 8 queens
    #population = random_population(num_of_queens, population_size)
    #individual, generation_num = genetic_algorithm(population, max_fitness)
    #print_most_fit(individual, generation_num)
    Initial_state = [1, 2, 3, 4, 5]
    goal_state = [3, 2, 1, 4, 6]
    num_matching_tiles = initial_fitness(Initial_state, goal_state)
    print(f"The number of matching elements is: {num_matching_tiles}")


if __name__ == '__main__':
    main()
