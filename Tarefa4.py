import pygad
import numpy as np

def Calc_Coefs(k, p):
    A0 = (5 * k) / 8
    A1 = k * (p - 0.5)
    A2 = 3 * k / 8

    CL = 2 * np.pi * (A0 + A1 / 2)
    CM = np.pi / 4 * (A2 - A1)**2

    return CL, CM


def fitness_func(solution, solution_idx):
    k = solution[0]
    p = solution[1]

    CL, CM = Calc_Coefs(k, p)
    CLref = 1.4

    return - (abs(CL - CLref) + CM**2)

last_fitness = 0

def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]


ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=10,
                       fitness_func=fitness_func,
                       sol_per_pop=10,
                       num_genes=2,
                       gene_space=[{"low": 0, "high": 0.3}, {"low": 0.05, "high": 2.}],
                       mutation_by_replacement=True,
                       on_generation=on_generation)

ga_instance.run()
ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)

print("Solution", solution)
print(f"Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

