import random

def initialize_population(size, target_sequence):
    return [random.sample(target_sequence, len(target_sequence)) for _ in range(size)]

def fitness(sequence, target):
    return sum(abs(a - b) for a, b in zip(sequence, target))

def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    return random.choices(population, weights=probabilities, k=2)

def one_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child

def two_point_crossover(parent1, parent2):
    point1 = random.randint(0, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)
    child = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    return child

def mutate(sequence, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(sequence)), 2)
        sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence
