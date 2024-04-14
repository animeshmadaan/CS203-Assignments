import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Take input from the user for A and B within the range (0, 1)
while True:
    A = float(input("Enter the value of A (0 < A < 1): "))
    if 0 < A < 1:
        break
    else:
        print("Please enter a value for A within the range (0, 1)")

while True:
    B = float(input("Enter the value of B (A < B < 1): "))
    if A < B < 1:
        break
    else:
        print("Please enter a value for B greater than A within the range (A, 1)")

# Take input from the user for mean and standard deviation
MEAN = float(input("Enter the mean: "))
while True:
    STD = float(input("Enter the standard deviation (must be positive): "))
    if STD > 0:
        break
    else:
        print("Standard deviation must be positive. Please enter a valid value.")


# Define bins for plotting the histogram
BINS = 1000

# Sample numbers from A uniform distribution
N = 100000
random_numbers = np.random.uniform(A, B, N)

# Calculate the inverse of the cumulative distribution function (CDF) of the Gaussian Distribution for each number
gaussian_random_numbers = norm.ppf(random_numbers, loc = MEAN, scale = STD)

# Plot a histogram using the random numbers generated
print("Mean of sampled distribution is", np.mean(gaussian_random_numbers))
print("Standard deviation of sampled distribution is", np.std(gaussian_random_numbers))

plt.hist(gaussian_random_numbers, bins = BINS)
plt.title('Gaussian Distribution within the interval [{}, {}]'.format(A, B))
plt.xlabel('Random Number')
plt.ylabel('Frequency')
plt.savefig("plot.png")
plt.show()