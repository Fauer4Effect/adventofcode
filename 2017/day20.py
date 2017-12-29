"""
Author: Kyle Fauerbach
Python solution to advent of code day 20
"""

class Particle(object):
    """
    A single particle
    Attributes:
        x, y, z coordinates
        vel_x, vel_y, vel_z velocities
        acc_x, acc_y, acc_z acceleration
    Methods:
        do_tick() updates velocity and position every tick
    """
    def __init__(self, position, velocity, acceleration):
        """
        take three arguments, each of which is a list
        position[x, y, z] velocity[x, y, z] acceleration[x, y, z]
        """
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.vel_x = velocity[0]
        self.vel_y = velocity[1]
        self.vel_z = velocity[2]
        self.acc_x = acceleration[0]
        self.acc_y = acceleration[1]
        self.acc_z = acceleration[2]
    def do_tick(self):
        self.vel_x += self.acc_x
        self.vel_y += self.acc_y
        self.vel_z += self.acc_z
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

def distance(particle):
    """
    Calculates the 3D manhattan distance between the particle and (0, 0, 0)
    """
    return abs(particle.x) + abs(particle.y) + abs(particle.z)

def part1():
    """
    answer should be 150
    """
    particles = []
    with open("20_1_in.txt", "r") as my_input:
        data = map(str.strip, my_input.readlines())
    for particle in data:
        particle = particle.split(', ')
        position = particle[0][3:-1]
        position = map(int, position.split(','))
        velocity = particle[1][3:-1]
        velocity = map(int, velocity.split(','))
        acceleration = particle[2][3:-1]
        acceleration = map(int, acceleration.split(','))
        particles += [Particle(position, velocity, acceleration)]
    for particle in particles:
        for _ in range(2000):
            particle.do_tick()
    distances = {}
    for i in xrange(len(particles)):
        distances[distance(particles[i])] = i
    closest = min(distances.keys())
    return distances[closest]

def part2():
    """
    answer should be 657
    """
    particles = []
    with open("20_1_in.txt", "r") as my_input:
        data = map(str.strip, my_input.readlines())
    for particle in data:
        particle = particle.split(', ')
        position = particle[0][3:-1]
        position = map(int, position.split(','))
        velocity = particle[1][3:-1]
        velocity = map(int, velocity.split(','))
        acceleration = particle[2][3:-1]
        acceleration = map(int, acceleration.split(','))
        particles += [Particle(position, velocity, acceleration)]
    collided = set()
    for _ in range(2000):
        locations = {}
        for i in xrange(len(particles)):
            particles[i].do_tick()
            location = ','.join(map(str, [particles[i].x, particles[i].y, particles[i].z]))
            if location not in locations.keys():
                locations[location] = [i]
            else:
                locations[location] += [i]
        for parts in locations.itervalues():
            if len(parts) > 1:
                for part in parts:
                    collided.add(part)
    return len(particles) - len(collided)

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
