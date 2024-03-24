import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
from numpy import sin, cos, pi, linspace
RADIUS = 1

def rotate_cartesian(cartesian_tuple, theta):
    x, y = cartesian_tuple
    x_prime = x * np.cos(theta) - y * np.sin(theta)
    y_prime = x * np.sin(theta) + y * np.cos(theta)
    return x_prime, y_prime

def generate_point(rng,radius):
    point = []
    x = rng.uniform(-radius, radius)
    y = rng.uniform(-radius, radius)
    while x**2 + y**2 > radius**2:
        x = rng.uniform(-radius, radius)
        y = rng.uniform(-radius, radius)
    point.append(x)
    point.append(y)
    return point

def draw_chord(point, radius, color = "black"):
    dist = math.sqrt(point[0]**2 + point[1]**2)
    projected_point = (point[0] * radius / dist, point[1] * radius / dist)
    theta = math.acos(dist/radius)
    point_1 = rotate_cartesian(projected_point, -theta)
    point_2 = rotate_cartesian(projected_point, theta)
    plt.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], color = color, lw = 0.5)

def mid_point_method() :
    rng = np.random.default_rng()

    # Let radius be 1 unit.
    # Random Mid-Point Method
    # 
    # Let us draw the chord in such a way that a random point is chosen inside the circle, then a chord is drawn perpendicular to the line joining center and the the point, passing through the point. Then any chord with mid point lying more than half the radius from center is greater than equilateral triangle.

    n = 1000
    Sample = []
    for i in range(n):
        Sample.append(generate_point(rng,RADIUS))

    distance = []
    for i in range(n):
        distance.append(math.sqrt(Sample[i][0]**2 + Sample[i][1]**2))


    distribution = []
    for i in range(n):
        distribution.append(distance[i] < 0.5)

    #plotting chords

    #draw circle
    r = 1
    angles = linspace(0 * pi, 2 * pi, 100)
    xs = r * cos(angles)
    ys = r * sin(angles)

    for i in range(n):
        if distribution[i]:
            draw_chord(Sample[i], RADIUS, "blue")
        else:
            draw_chord(Sample[i], RADIUS, "red")

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

    #plotting trials

    avg = [sum(distribution[:i])/i for i in range(1,n+1)]

    plt.title("The Random Mid-Point Method")
    plt.xlabel("Number of Trials")
    plt.ylabel("Proportion of Chords Longer than the side")
    plt.axis([0,n,0,1])

    plt.xticks([0,100,200,300,400,500,600,700,800,900,1000])
    plt.yticks([0,0.25,0.5,0.75,1])
    plt.plot(range(1,n+1), avg)
    plt.show()