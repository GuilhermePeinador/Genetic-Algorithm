import pygad
from matplotlib import pyplot as plt
import numpy as np


def Calc_Coefs(k, p):
    A0 = (5 * k) / 8
    A1 = k * (p - 0.5)
    A2 = 3 * k / 8

    CL = 2 * np.pi * (A0 + A1 / 2)
    CM = np.pi / 4 * (A2 - A1) ** 2

    return CL, CM


def fitness_func(solution, solution_idx):
    k = solution[0]
    p = solution[1]

    CL, CM = Calc_Coefs(k, p)
    CLref = 1.4

    return - (abs(CL - CLref) / CLref + 1e3 * abs(CM))


last_fitness = 0

Cl_array=[]
Cm_array=[]

for i in range(30):

    def on_generation(ga_instance):
        global last_fitness
        print("Generation = {generation}".format(generation=ga_instance.generations_completed))
        print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
        print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
        last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]


    ga_instance = pygad.GA(num_generations=70,
                           num_parents_mating=30,
                           fitness_func=fitness_func,
                           sol_per_pop=50,
                           num_genes=2,
                           gene_space=[{"low": 0, "high": 0.3}, {"low": 0.05, "high": 2.}],
                           mutation_by_replacement=True,
                           on_generation=on_generation,
                           save_solutions=True)

    ga_instance.run()
    #ga_instance.plot_fitness()
    #ga_instance.plot_genes(graph_type="boxplot")
    #ga_instance.plot_genes(graph_type="histogram", solutions='all')

    solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)

    Cl, Cm = Calc_Coefs(solution[0], solution[1])
    Cl_array.append(Cl)
    Cm_array.append(Cm)

    print("Solution", solution)
    print(f"Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    print("Coefs Values -> Cl = {:f}  Cm = {:f}".format(Cl, Cm))
    print("Cl array = ",Cl_array)
    print("Cm array = ",Cm_array)


n_bins = 50

fig, ((ax0, ax1)) = plt.subplots(ncols=2)

colors=['red']
ax0.hist(Cl_array, n_bins, density = True, histtype='bar', color=colors)
ax0.set_title('Histrograma de Cl')

colors=['blue']
ax1.hist(Cm_array, n_bins, density = True, histtype='bar', color=colors)
ax1.set_title('Histrograma de Cm')

fig.tight_layout()
plt.show()