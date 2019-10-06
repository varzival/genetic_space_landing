import numpy as np
import enum
import Physics
import GUI
import pygame
import configs

class State(enum.Enum):
    running = 0
    landed = 1
    crashed = 2
    outOfBounds = 3


class Simulation:
    def __init__(self):
        self.reset()

    def reset(self):
        self.rocket_pos = configs.rocket_pos.copy()
        self.rocket_velocity = configs.rocket_velocity.copy()
        self.rocket_acceleration = configs.rocket_acceleration.copy()
        self.state = State.running

    def evaluateFitness(self):
        fitness = 100000
        pos_dist = Physics.manhattanDistance(self.rocket_pos, configs.rocket_size, configs.ground_pos, configs.ground_size)
        fitness -= pos_dist * 100
        fitness -= abs(self.rocket_velocity[0]) * 8 + abs(self.rocket_velocity[1]) * 8
        if self.state == State.landed:
            fitness += 100000
        return fitness

    def run_with_commands(self, commands):
        self.reset()
        t = 1.0 / float(configs.FPS)
        frames = 0
        while len(commands) > 0 and self.state == State.running:
            self.run_step(t, commands.pop(0))
            frames += 1
        while self.state == State.running:
            self.run_step(t, np.array((0.0, 0.0)))
        return frames

    def run_with_commands_GUI(self, commands):
        GUI.init(configs.window_size)
        self.reset()
        clock = pygame.time.Clock()
        frames = 0

        while len(commands) > 0 and self.state == State.running:
            t = clock.tick(configs.FPS) / 1000.0
            command = commands.pop(0)
            self.run_step(t, command)
            GUI.update(self.rocket_pos, configs.rocket_size, configs.ground_pos, configs.ground_size)
            frames += 1
        while self.state == State.running:
            t = clock.tick(configs.FPS) / 1000.0
            self.run_step(t, np.array((0.0, 0.0)))
            GUI.update(self.rocket_pos, configs.rocket_size, configs.ground_pos, configs.ground_size)
            frames += 1
        if self.state == State.landed:
            print("Landed!")
            print("Velocity: " + str(self.rocket_velocity))
        elif self.state == State.crashed:
            print("Crashed.")
            print("Velocity: " + str(self.rocket_velocity))
        elif self.state == State.outOfBounds:
            print("Outside of bounds.")
            print("Velocity: " + str(self.rocket_velocity))

        print("Fitness: " + str(self.evaluateFitness()))
        print("Frames: " + str(frames))


    def run_step(self, t, command):
        if not self.state == State.running:
            return
        if Physics.collisionDetection(self.rocket_pos, configs.rocket_size, configs.ground_pos, configs.ground_size):
            if Physics.checkLanding(self.rocket_velocity, configs.landing_tolerance):
                self.state = State.landed
            else:
                self.state = State.crashed

        if not Physics.checkInsideBounds(self.rocket_pos, configs.window_size):
            self.state = State.outOfBounds

        self.rocket_acceleration = command * 2.0
        self.rocket_velocity, self.rocket_pos = \
            Physics.calculate_delta(t, self.rocket_velocity, self.rocket_pos, self.rocket_acceleration)