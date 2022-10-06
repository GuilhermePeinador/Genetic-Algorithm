import pygad
import numpy

def fitness_func (solution, solution_idx):
    x = solution[0]
    y = -(x*numpy.sin(3*x))
    return y

last_fitness = 0
def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]

ga_instance = pygad.GA(num_generations = 50,
                       num_parents_mating = 5,
                       fitness_func = fitness_func,
                       sol_per_pop = 10,
                       num_genes = 1,
                       gene_space = {"low": 0, "high": numpy.pi},
                       mutation_by_replacement = True,
                       on_generation = on_generation)

ga_instance.run()
ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
print("Solution", solution)
print(f"Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))