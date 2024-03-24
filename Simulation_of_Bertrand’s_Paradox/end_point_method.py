import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
from numpy import sin, cos, pi, linspace
RADIUS = 1

def generate_angle(rng):
    angle = rng.uniform(-pi, pi)
    return angle

def end_point_method():
    rng = np.random.default_rng()
    # Let radius be 1 unit

    # The Random Endpoint Method
    # 
    # Let us take two points on the periphery and rotate the traingle such that one coincides with one of the vertices. Now if the other endpoint lies on the minor arc subtended by other two vertices of the triangle then the chord is longer than the sides, otherwise it is shorter.
    # 
    # To take a second end point let us sample the angle $theta$ taken counter anti-clockwise from positive x-axis. And if $theta$ lies between $pi/3$ and $-pi/3$ then the chord is longer, otherwise it ios shorter.
    #draw point at orgin
    plt.plot(0,0, color = 'red', marker = 'o')
    plt.gca().annotate('O', xy=(0 - 0.1, 0 - 0.2), xycoords='data', fontsize=10)

    #draw circle
    r = 1
    angles = linspace(0 * pi, 2 * pi, 100)
    xs = r * cos(angles)
    ys = r * sin(angles)

    #draw triangle
    plt.plot(xs, ys, color = 'black')
    plt.plot(r * cos(pi /3), r * sin(pi / 3), marker = 'o', color = 'black')
    plt.plot(r * cos(-pi /3), r * sin(-pi / 3), marker = 'o', color = 'black')
    plt.plot(r * cos(pi), r * sin(pi), marker = 'o', color = 'black')
    plt.plot([-1, r * cos(pi /3)], [0, r * sin( pi / 3)], color = "black")
    plt.plot([-1, r * cos(-pi /3)], [0, r * sin(-pi / 3)], color = "black")
    plt.plot([r * cos(pi /3), r * cos(pi /3)], [r * sin(-pi / 3), r * sin( pi / 3)], color = "black")

    #draw radius
    plt.plot([0, 1], [0, 0], color = 'purple')

    #draw arc
    arc_angles = linspace(0 * pi, pi/6, 20)
    arc_xs = r * cos(arc_angles)
    arc_ys = r * sin(arc_angles)
    plt.plot(arc_xs, arc_ys, color = 'red', lw = 3)

    #draw another radius
    plt.plot(1, 0, marker = 'o', color = 'black')
    plt.plot(r * cos(pi /6), r * sin( pi / 6), marker = 'o', color = 'black')
    plt.plot([0, r * cos(pi /6)], [0, r * sin( pi / 6)], color = "purple")
    # draw theta angle and annotation
    r1 = 0.3
    arc_angles = linspace(0 * pi, pi/6, 20)
    arc_xs = r1 * cos(arc_angles)
    arc_ys = r1 * sin(arc_angles)
    plt.plot(arc_xs, arc_ys, color = 'green', lw = 3)
    plt.gca().annotate(r'$\theta$', xy=(0.35, 0.07), xycoords='data', fontsize=15, rotation = 0)

    plt.plot([-1, r * cos(pi / 6)], [0, r * sin(pi / 6)], color = "black")

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal')
    plt.show()
    
    m = 1000
    Sample = []
    for i in range(m):
        Sample.append(generate_angle(rng))


    distribution = []
    for i in range(m):
        distribution.append(Sample[i] < pi/3 and Sample[i] > -pi/3)

    #plotting chords

    #draw circle
    r = 1
    angles = linspace(0 * pi, 2 * pi, 100)
    xs = r * cos(angles)
    ys = r * sin(angles)

    for i in range(m):
        ref_point = (-RADIUS, 0)
        theta = Sample[i]
        point = RADIUS*(np.cos(theta),np.sin(theta))
        colour = 'red'
        if ( distribution[i]) :
            colour = 'blue'
        plt.plot([point[0],ref_point[0]],[point[1],ref_point[1]], color = colour, lw = 0.5)

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


    avg = [sum(distribution[:i])/i for i in range(1,m+1)]

    plt.title("The Random End-Point Method")
    plt.xlabel("Number of Trials")
    plt.ylabel("Proportion of Chords Longer than the side")
    plt.axis([0,m,0,1])

    plt.xticks([0,100,200,300,400,500,600,700,800,900,1000])
    plt.yticks([0,0.33,0.66,1])
    plt.plot(range(1,m+1), avg)
    plt.show()