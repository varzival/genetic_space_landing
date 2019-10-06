from Genome import *
import pickle
import configs

solutionGenome = pickle.load(open("./solutions/solution1.pickle", "rb"), encoding="utf-8")
configs.ground_pos = np.array((300, 390))
configs.ground_size = np.array((100, 40))
Simulation().run_with_commands_GUI(solutionGenome.getCommandList())

solutionGenome = pickle.load(open("./solutions/solution2.pickle", "rb"), encoding="utf-8")
configs.ground_pos = np.array((400, 290))
configs.ground_size = np.array((50, 40))
Simulation().run_with_commands_GUI(solutionGenome.getCommandList())