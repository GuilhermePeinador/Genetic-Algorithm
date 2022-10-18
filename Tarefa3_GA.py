import pygad
import matplotlib.pyplot as plt


def fitness_func(solution, solution_idx):
    mu = 1
    x = solution[0]
    y = solution[1]
    func = x + y
    fitness = - ( func + (mu/2) * (x ** 2 + y ** 2 - 2)**2 )
    return fitness


last_fitness = 0


def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(
        fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(
        change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]


ga_instance = pygad.GA(num_generations=100,
                       num_parents_mating=5,
                       fitness_func=fitness_func,
                       sol_per_pop=10,
                       num_genes=2,
                       gene_space={"low": -5, "high": 5},
                       mutation_by_replacement=True,
                       on_generation=on_generation)

ga_instance.run()
ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)

print("Solution", solution)
print(f"Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

