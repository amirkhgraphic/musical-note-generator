import random

def initialize_population(n, target_sequence):
    return [random.sample(target_sequence, len(target_sequence)) for _ in range(n)]

def fitness(sequence, target):
    return sum(abs(a - b) for a, b in zip(sequence, target))

def roulette_wheel_selection(population, fitnesses):
    max_fitness = max(fitnesses)
    inverted_fitnesses = [max_fitness - f for f in fitnesses]
    probabilities = [f / sum(inverted_fitnesses) for f in inverted_fitnesses] if sum(inverted_fitnesses) else [1 / len(population)] * len(population)
    return random.choices(population, weights=probabilities, k=2)

def one_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]
    return offspring1, offspring2

def two_point_crossover(parent1, parent2):
    point1 = random.randint(0, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)
    offspring1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    offspring2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return offspring1, offspring2

def order_one_crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 2)
    end = random.randint(start + 1, len(parent1) - 1)
    offspring1 = parent1[:start] + [x for x in parent2 if x not in parent1[:start]] + parent1[end:]
    offspring2 = parent2[:start] + [x for x in parent1 if x not in parent2[:start]] + parent2[end:]
    return offspring1, offspring2

def partially_mapped_crossover(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), k=2))

    offspring1 = [None] * start + parent1[start:end] + [None] * (n - end)
    offspring2 = [None] * start + parent2[start:end] + [None] * (n - end)

    def fill_offspring(offspring, parent, other_parent):
        for i, gene in enumerate(parent[start:end]):
            if gene in offspring:
                continue

            i += start
            while start <= i < end:
                i = parent.index(other_parent[i])
            offspring[i] = gene

        return [offspring[i] or parent[i] for i in range(n)]

    offspring1 = fill_offspring(offspring1, parent2, parent1)
    offspring2 = fill_offspring(offspring2, parent1, parent2)

    return offspring1, offspring2

def mutate(sequence, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(sequence)), 2)
        sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence

def get_crossover(i):
    crossovers = [
        one_point_crossover,
        two_point_crossover,
        order_one_crossover,
        partially_mapped_crossover,
    ]

    return crossovers[int(i)]