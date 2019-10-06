import numpy as np
import random
import copy
import configs
from Simulation import Simulation

act = np.array([-1.0, 0.0, 1.0])
# carthesian product
actions = np.transpose([np.tile(act, len(act)), np.repeat(act, len(act))])

class Gene:

    def __init__(self):
        self.action = None
        self.duration = None
        self.mutateAction()
        self.mutateDuration()

    def mutateAction(self):
        self.action = random.choice(actions)

    def mutateDuration(self):
        self.duration = random.randint(1, configs.maxActionDuration)

    def __eq__(self, other):
        return np.array_equal(self.action, other.action) and self.duration == other.duration

class Genome:

    def __init__(self, genes=None):
        if genes:
            self.genes = copy.deepcopy(genes)
        else:
            self.genes = []
            for _ in range(configs.numberOfGenes):
                self.genes.append(Gene())
        self.fitness = None

    def getCommandList(self):
        commands = []
        for gene in self.genes:
            for _ in range(gene.duration):
                commands.append(gene.action)

        return commands

    def evaluateFitness(self):
        if not self.fitness:
            sim = Simulation()
            commands = self.getCommandList()
            sim.run_with_commands(commands)

            self.fitness = sim.evaluateFitness()

    def mutate(self):
        for gene in self.genes:
            if random.random() < configs.mutationRate:
                gene.mutateAction()
            if random.random() < configs.mutationRate:
                gene.mutateDuration()

        return self
