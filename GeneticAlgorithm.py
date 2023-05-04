import random


class Individual:
    def __init__(self, state):
        self.state = state
        self.fitness = self.fitness(state)

    def fitness(state):
        matching_tiles = 0
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == goal_state[i][j]:
                    matching_tiles += 1
        return matching_tiles


def crossover(parent1: Individual, parent2: Individual) -> Individual:
    crossover_point = random.randint(0, len(parent1.state) - 1)
    return Individual(parent1.state[0:crossover_point] + parent2.state[crossover_point:])


def mutation():
    Sample


def genetic_algorithm():
    Sample


state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
print(Individual.fitness(state))
#print(crossover())
