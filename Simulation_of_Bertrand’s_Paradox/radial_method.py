import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
from numpy import sin, cos, pi, linspace
RADIUS = 1  

def radial_method ():
    rng = np.random.default_rng()

    # The Random Radial Point Method
    # 
    # In this approach we draw a chord perpendicular to endpoint of some radius less than or equal to $r$. We sample radius from uniform distribution over [0,radius]. 
    # 
    # Any radius less than $radius/2$ has a corresponding chord that is greater than the side.

    l = 1000
    Sample = []
    for i in range(l):
        Sample.append(rng.uniform(0, RADIUS))


    distribution = []
    for i in range(l):
        distribution.append(Sample[i] < RADIUS/2)

    #plotting chords

    #draw circle
    r = RADIUS
    angles = linspace(0 * pi, 2 * pi, 100)
    xs = r * cos(angles)
    ys = r * sin(angles)

    for i in range(l):
        colour = "red"
        if (distribution[i]):
            colour = "blue"
        point = (Sample[i], math.sqrt(RADIUS**2  - Sample[i]**2))
        plt.plot([point[0],point[0]], [point[1],-point[1]], color = colour, lw = 0.1)

    #draw triangle
    plt.plot(xs, ys, color = 'black')
    # plt.plot(r * cos(pi /3), r * sin(pi / 3), marker = 'o', color = 'black')
    # plt.plot(r * cos(-pi /3), r * sin(-pi / 3), marker = 'o', color = 'black')
    # plt.plot(r * cos(pi), r * sin(pi), marker = 'o', color = 'black')
    plt.plot([-1, r * cos(pi /3)], [0, r * sin( pi / 3)], color = "black")
    plt.plot([-1, r * cos(-pi /3)], [0, r * sin(-pi / 3)], color = "black")
    plt.plot([r * cos(pi /3), r * cos(pi /3)], [r * sin(-pi / 3), r * sin( pi / 3)], color = "black")

    #plt.plot([-1, r * cos(pi / 6)], [0, r * sin(pi / 6)], color = "blue")

    plt.xlim(-1.5*RADIUS, 1.5*RADIUS)
    plt.ylim(-1.5*RADIUS, 1.5*RADIUS)
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.show()


    avg = [sum(distribution[:i])/i for i in range(1,l+1)]

    plt.title("The Random Radial Point Method")
    plt.xlabel("Number of Trials")
    plt.ylabel("Proportion of Chords Longer than the side")
    plt.axis([0,l,0,1])

    plt.xticks([0,100,200,300,400,500,600,700,800,900,1000])
    plt.yticks([0,0.25,0.5,0.75,1])
    plt.plot(range(1,l+1), avg)
    plt.show()