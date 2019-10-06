from Genome import *
from typing import List
import pickle
import copy

def evolve():
    #first generation
    population = []
    for _ in range(populationSize):
        population.append(Genome())

    generationCounter = 1
    bestIndividual = population[0]
    bestFitness = 0

    while generationCounter <= generations:
        for ind in population:
            ind.evaluateFitness()
        population.sort(key=lambda x: x.fitness, reverse=True)

        if population[0].fitness > bestFitness:
            bestIndividual = population[0]
            bestFitness = population[0].fitness
        print("Generation: " + str(generationCounter))
        print("Best Fitness: " + str(population[0].fitness))
        #if generationCounter % 20 == 0:
        #    Simulation().run_with_commands_GUI(population[0].getCommandList())

        if bestFitness > 100000:
            print("Solution found!")
            pickle.dump(bestIndividual, open("solution.pickle", "wb"))
            Simulation().run_with_commands_GUI(bestIndividual.getCommandList())
            break

        newPopulation = population[:saveBestPopulationSize]
        while len(newPopulation) < len(population):
            genome1 = elitistSelection(population)
            genome2 = elitistSelection(population)
            offspring1, offspring2 = crossOver(genome1, genome2)
            newPopulation.append(offspring1)
            newPopulation.append(offspring2)

        population = newPopulation
        generationCounter += 1

    pickle.dump(bestIndividual, open("bestRun.pickle", "wb"))
    Simulation().run_with_commands_GUI(bestIndividual.getCommandList())


def crossOver(genome1: Genome, genome2: Genome):
    if random.random() > crossOverRate:
        return copy.deepcopy(genome1).mutate(), copy.deepcopy(genome2).mutate()

    offspring1 = []
    offspring2 = []

    for i in range(numberOfGenes):
        if random.random() > swapRate:
            offspring1.append(genome1.genes[i])
            offspring2.append(genome2.genes[i])
        else:
            offspring1.append(genome2.genes[i])
            offspring2.append(genome1.genes[i])

    return Genome(offspring1).mutate(), Genome(offspring2).mutate()

def elitistSelection(population: List[Genome]):
    totalFitness = 0
    for ind in population:
        totalFitness += ind.fitness

    randomSlice = random.random() * totalFitness
    fitnessSum = 0
    for ind in population:
        fitnessSum += ind.fitness
        if fitnessSum >= randomSlice:
            return ind

    return population[0]

if __name__ == "__main__":
    evolve()