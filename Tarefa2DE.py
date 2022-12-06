import pygad
from matplotlib import pyplot as plt
import numpy


def fitness_func(solution, solution_idx):
    x = solution[0]
    y = -(x * numpy.sin(3 * x))
    return y


last_fitness = 0

# sol_array = []

# for i in range(30):
def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(
        fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(
        change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]


ga_instance = pygad.GA(num_generations=10,
                       num_parents_mating=30,
                       fitness_func=fitness_func,
                       sol_per_pop=50,
                       num_genes=1,
                       gene_space={"low": 0, "high": 2 * numpy.pi},
                       on_generation=on_generation,
                       mutation_type="adaptive",
                       mutation_probability=[0.25, 0.1],
                       save_solutions=True)

ga_instance.run()
ga_instance.plot_fitness()
# ga_instance.plot_new_solution_rate()

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)

# sol_array.append(solution_fitness)

print("Solution", solution)
print(f"Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
# print('Solutions array = ', sol_array)
