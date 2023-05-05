import random

# Class definition of a class which represents an individual in the population
class Individual:
    # A constructor that initializes an individual's state and fitness
    def __init__(self, state):
        self.state = state
        self.fitness = self.fitness(state)

    # Fitness function that calculates an individual's fitness based on the number of tiles in correct positions
    def fitness(self, state):
        correct_positions = 0
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == goal_state[i][j]: # If the tile is in the correct position compared to goal_state
                    correct_positions += 1
                elif state[i][j] != 0: # If the tile is not the blank tile (0) and can be moved into the blanks position
                    if (i > 0 and state[i - 1][j] == 0) or \
                            (j > 0 and state[i][j - 1] == 0) or \
                            (i < len(state) - 1 and state[i + 1][j] == 0) or \
                            (j < len(state[0]) - 1 and state[i][j + 1] == 0):
                        correct_positions += 1
        return correct_positions

# Reproduce function which produces offspring by randomly selecting a crossover point and "swapping chromosomes" from each parent
def reproduce(first_parent, second_parent):
    crossover_point = random.randint(0, len(first_parent.state) - 1)
    offspring = []
    for i in range(len(first_parent.state)):
        if i < crossover_point:
              offspring.append(first_parent.state[i])
        else:
            offspring.append(second_parent.state[i])
    return offspring

# Mutation function that randomly swaps two tiles
def mutate(offspring):
    # Find the position of the blank tile (0)
    blank_pos = None
    for i in range(len(offspring)):
        for j in range(len(offspring[0])):
            if offspring[i][j] == 0:
                blank_pos = (i, j)
                break
        if blank_pos is not None:
            break
    if blank_pos is None:
        return offspring  # return the original offspring if the empty tile is not found

    # Randomly swap two tiles that are not blank tiles (0)
    x1, y1 = random.sample(range(3), 2)
    x2, y2 = random.sample(range(3), 2)
    offspring[x1][y1], offspring[x2][y2] = offspring[x2][y2], offspring[x1][y1]
    return offspring


# Function that creates an inital state. This can also be changed to generate a random state instead.
def initial_state():
    return Individual([[3, 7, 1], [4, 5, 6], [2, 8, 0]])


# Population function which creates a population of random individuals
def random_population(population_size):
    return [initial_state() for _ in range(population_size)]


# retrieve_most_fit function which finds the most fit individual in the population
def retrieve_most_fit(population):
    most_fit_individual = population[0]
    for individuals in population:
        if individuals.fitness > most_fit_individual.fitness:
            most_fit_individual = individuals
    return most_fit_individual

# print_most_fit function prints the most fit individual as well as relevant details about current state of the population
def print_most_fit(individual, generation_num):
    print('Most fit configuration:')
    for row in individual.state:
        print(row)
    print('Fitness:')
    print(individual.fitness)
    print('Number of generations:')
    print(generation_num)


def genetic_algorithm(population, max_fitness):
    # Define mutation probability as well as generation start number
    mutation_probability = 0.05
    generation_numb = 1
    # Loop until solution is found or maximum number of generations is reached
    while max_fitness not in [individual.fitness for individual in population] and generation_numb < 10:
        # Create a new population
        new_population = []
        for _ in range(len(population)):
            # Select parents using fitness proportionate selection
            first_parent = fitness_proportionate_selection(population)
            second_parent = fitness_proportionate_selection(population)
            # Produce offspring using reproduction and mutation
            offspring = reproduce(first_parent, second_parent)
            if random.random() < mutation_probability:
                offspring = mutate(offspring)
            # Add offspring to the new population
            new_population.append(Individual(offspring))
        # Update population and generation number
        population = new_population
        generation_numb += 1
    # Return the most fit individual and the number of generations
    return retrieve_most_fit(population), generation_numb


def fitness_proportionate_selection(population):
    # Calculate the total fitness of the population
    total_fitness = sum(individual.fitness for individual in population)
    threshold = random.uniform(0, total_fitness)
    running_sum = 0
    # Iterate through the population and select an individual whose running_sum fitness is higher than the threshold
    for individual in population:
        running_sum += individual.fitness
        if running_sum > threshold:
            return individual
    # Return the first individual if no individual is selected
    return population[0]


# Driver code, define the goal_state, population_size and max_fitness
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
population_size = 100
max_fitness = 9
# Create a random population
population = random_population(population_size)
# Run the genetic algorithm and print the most fit individual as well as number of generations
individual, generation_num = genetic_algorithm(population, max_fitness)
print_most_fit(individual, generation_num)
