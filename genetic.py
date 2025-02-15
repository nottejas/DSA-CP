import random
 
def fitness(chromosome):
    attacks = 0
    n = len(chromosome)
    for i in range(n):
        for j in range(i+1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
                attacks += 1
    return attacks
 
def selection(population):
    population.sort(key=lambda x: fitness(x))
    return population[:2]
 
def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child
 
def mutation(chromosome):
    n = len(chromosome)
    mutation_point = random.randint(0, n-1)
    chromosome[mutation_point] = random.randint(0, n-1)
    return chromosome
 
def generate_population(size, n):
    population = []
    for _ in range(size):
        chromosome = [random.randint(0, n-1) for _ in range(n)]
        population.append(chromosome)
    return population
 
def genetic_algorithm(n, population_size, generations):
    population = generate_population(population_size, n)
    for generation in range(generations):
        print(f"Generation {generation+1}")
        best_solution = min(population, key=fitness)
        print(f"Best Solution: {best_solution} with Fitness: {fitness(best_solution)}")
        if fitness(best_solution) == 0:
            print("Solution found!")
            return best_solution
        parents = selection(population)
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = parents
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.append(mutation(child1))
            new_population.append(mutation(child2))
        population = new_population
    print("No solution found after max generations.")
    return None
 
n = 8
population_size = 100
generations = 1000
 
solution = genetic_algorithm(n, population_size, generations)
 
if solution:
    print(f"Solution: {solution}")
else:
    print("No solution found.")