import numpy as np
from pygame.constants import *

FPS = 30
window_size = (640, 480)
gravity = np.array((0, 1.635))
ground_pos = np.array((300, 390))
ground_size = np.array((100, 40))
rocket_pos = np.array((200, 100))
rocket_size = np.array((20, 30))
rocket_velocity = np.array((0.0, 0.0))
rocket_acceleration = np.array((0.0, 0.0))
landing_tolerance = np.array((48.0, 48.0))

key_mapping = {
                K_LEFT: np.array((-1.0, 0.0)),
                K_RIGHT: np.array((1.0, 0.0)),
                K_UP: np.array((0.0, -1.0)),
                K_DOWN: np.array((0.0, 1.0))
               }

# GENETICS
maxActionDuration = FPS
maxMutationDuration = FPS
numberOfGenes = 10
mutationRate = 0.1
populationSize = 100
saveBestPopulationSize = 10
generations = 1000
crossOverRate = 0.6
swapRate = 0.3