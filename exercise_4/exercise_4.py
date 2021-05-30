import numpy as np
import matplotlib.pyplot as plt
import random


def mutation(pop, number_of_individuals, F):
    index1 = np.random.randint(number_of_individuals)
    index2 = np.random.randint(number_of_individuals)
    index3 = np.random.randint(number_of_individuals)
    # print("1: ", index1)
    # print("2: ", index2)
    # print("3: ", index3)
    mut_vector = (pop[index1] - pop[index2]*F + pop[index3])
    # print("mut: ", mut_vector)
    return mut_vector


def crossover(father, mut_vector, number_of_variables):
    child = [father[i] if np.random.rand() < 0.8 else mut_vector[i] for i in range(number_of_variables)]
    # print("child: ", child)
    return child


def evaluation(variables):
    return -np.sum(np.square(variables))


def ackley(var):
    length = len(var)
    tmp1 = 20. - 20. * np.exp(-0.2 * np.sqrt(1. / length * np.sum(np.square(var))))
    tmp2 = np.e - np.exp(1. / length * np.sum(np.cos(np.array(var) * 2. * np.pi)))
    return -tmp1-tmp2


def salomon(var):
    var = np.array(var)
    return -(1.0 - np.cos(2.0 * np.pi * np.sqrt(sum(var ** 2.0))) + 0.1 * np.sqrt(sum(var ** 2.0)))


class DE:

    def __init__(self, number_of_variables, number_of_individuals, F, evaluation):
        self.number_of_variables = number_of_variables
        self.number_of_individuals = number_of_individuals
        self.pop = np.random.rand(number_of_individuals, number_of_variables)
        self.F = F
        self.evaluation = evaluation
        self.generations = 1000

    def optimize(self):
        graph = []
        for gen in range(self.generations):
            pop_eval = []
            # print("gen: ", gen)
            for index, individual in enumerate(self.pop):
                # print("index: ", index)
                # print("indiv: ", individual)
                # print("pop: ", self.pop)
                mut_vector = mutation(self.pop, self.number_of_individuals, self.F)
                child = crossover(individual, mut_vector, self.number_of_variables)
                if self.evaluation(child) > self.evaluation(individual):
                    self.pop[index] = child

                pop_eval.append(self.evaluation(self.pop[index]))

            avg_evaluation = np.mean(pop_eval)
            print(avg_evaluation)
            final_de = avg_evaluation
            graph.append(avg_evaluation)
            plt.plot(graph)
            plt.draw()
            plt.pause(0.00001)
            plt.clf()


        plt.plot(graph)
        plt.show()
        
def exercise_4(inputs): # DO NOT CHANGE THIS LINE
    """
    This functions receives the input in the parameter 'inputs'. 
    Change the code, so that the output is sqaure of the given input.

    Output should be the name of the class.
    """
    F = 1.0
    number_of_variables = 2
    number_of_individuals = 100
    de = DE(number_of_variables, number_of_individuals, F, ackley)
    de.optimize()
    
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
