from configs import *
import GUI
import pygame
from Simulation import Simulation, State
from Physics import manhattanDistance

clock = pygame.time.Clock()

def handleEvent(event):
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        return False

    global command

    if event.type == KEYDOWN:
        for key in key_mapping:
            if event.key == key:
                command += key_mapping[key]
    if event.type == KEYUP:
        for key in key_mapping:
            if event.key == key:
                command -= key_mapping[key]

    return True


def main():
    global command

    command = np.array((0.0, 0.0))
    GUI.init(window_size)

    sim = Simulation()
    frames = 0
    commands = []

    while True:
        t = clock.tick(FPS) / 1000.0

        if not handleEvent(pygame.event.poll()):
            break

        sim.run_step(t, command)

        if sim.state == State.landed:
            print(sim.rocket_velocity)
            print("Landed!")
            break
        elif sim.state == State.crashed:
            print(sim.rocket_velocity)
            print("Crashed.")
            break
        elif sim.state == State.outOfBounds:
            print("Outside of bounds.")
            break

        GUI.update(sim.rocket_pos, rocket_size, ground_pos, ground_size)
        frames += 1
        commands.append(command.copy())

    print("Frames: "+str(frames))
    #sim.run_with_commands_GUI(commands)


if __name__ == '__main__':
    main()
