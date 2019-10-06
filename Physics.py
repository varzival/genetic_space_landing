from configs import *

def calculate_delta(t, velocity, pos, acc):
    global gravity
    # t = delta time since last frame
    h = 0.5 * (gravity + acc) * t**2 + velocity * t + pos
    v = (gravity + acc) + velocity

    return v, h


def collisionDetection(rocket_pos, rocket_size, ground_pos, ground_size):
    ground_span_hor = (ground_pos[0], ground_pos[0] + ground_size[0])
    ground_span_vert = (ground_pos[1], ground_pos[1] + ground_size[1])
    rocket_span_hor = (rocket_pos[0], rocket_pos[0] + rocket_size[0])
    rocket_span_vert = (rocket_pos[1], rocket_pos[1] + rocket_size[1])
    if rocket_span_hor[1] < ground_span_hor[0] or rocket_span_hor[0] > ground_span_hor[1]:
        return False
    if rocket_span_vert[1] < ground_span_vert[0] or rocket_span_vert[0] > ground_span_vert[1]:
        return False
    return True


def checkLanding(rocket_velocity, landing_tolerance):
    vel = np.abs(rocket_velocity)
    return vel[0] < landing_tolerance[0] and vel[1] < landing_tolerance[1]


def checkInsideBounds(rocket_pos, window_size):
    return 0.0 < rocket_pos[0] < window_size[0] and 0 < rocket_pos[1] < window_size[1]


def manhattanDistance(rocket_pos, rocket_size, ground_pos, ground_size):
    ground_span_hor = (ground_pos[0], ground_pos[0] + ground_size[0])
    ground_span_vert = (ground_pos[1], ground_pos[1] + ground_size[1])
    rocket_span_hor = (rocket_pos[0], rocket_pos[0] + rocket_size[0])
    rocket_span_vert = (rocket_pos[1], rocket_pos[1] + rocket_size[1])
    dist = 0.0

    if rocket_span_hor[1] < ground_span_hor[0]:
        dist += ground_span_hor[0] - rocket_span_hor[1]
    if rocket_span_hor[0] > ground_span_hor[1]:
        dist += rocket_span_hor[0] - ground_span_hor[1]
    if rocket_span_vert[1] < ground_span_vert[0]:
        dist += ground_span_vert[0] - rocket_span_vert[1]
    if rocket_span_vert[0] > ground_span_vert[1]:
        dist += rocket_span_vert[0] - ground_span_vert[1]

    return dist