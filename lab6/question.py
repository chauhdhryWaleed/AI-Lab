import random

class NQueensGeneticAlgorithm:
    def __init__(self, n_queens, population_size=100, mutation_rate=0.01):
        self.n_queens = n_queens
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self._initialize_population()
        self.max_fitness = n_queens * (n_queens - 1) // 2

    def _initialize_population(self):
        return [self._generate_chromosome() for _ in range(self.population_size)]

    def _generate_chromosome(self):
        chromosome = list(range(self.n_queens))
        random.shuffle(chromosome)
        return chromosome

    def _fitness(self, chromosome):
        attacks = sum(1 for i in range(self.n_queens) for j in range(i + 1, self.n_queens)
                      if abs(i - j) == abs(chromosome[i] - chromosome[j]))
        return self.max_fitness - attacks

    def _select_parent(self):
        total_fitness = sum(self._fitness(chromosome) for chromosome in self.population)
        selection_probabilities = [self._fitness(chromosome) / total_fitness for chromosome in self.population]
        return random.choices(self.population, weights=selection_probabilities)[0]

    def _crossover(self, parent1, parent2):
        crossover_point = random.randint(0, self.n_queens - 1)
        child = parent1[:crossover_point]
        child += [gene for gene in parent2 if gene not in child]
        return child

    def _mutate(self, chromosome):
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(self.n_queens), 2)
            chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

    def evolve(self, generations):
        for _ in range(generations):
            new_population = [self._crossover(self._select_parent(), self._select_parent()) for _ in range(self.population_size)]
            for chromosome in new_population:
                self._mutate(chromosome)
            self.population = new_population

            # Check for solution
            for chromosome in self.population:
                if self._fitness(chromosome) == self.max_fitness:
                    return chromosome

        # No solution found after all generations
        return None

def print_board(chromosome):
    n = len(chromosome)
    for row in range(n):
        line = ''.join('Q ' if chromosome[col] == row else '. ' for col in range(n))
        print(line)
    print()

if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard (N): "))
    genetic_algorithm = NQueensGeneticAlgorithm(n)
    solution = genetic_algorithm.evolve(generations=1000)
    if solution:
        print("Solution found:")
        print_board(solution)
    else:
        print("No solution found within the given generations.")
