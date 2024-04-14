import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Observation
observation = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]  # 1 for H, 0 for T

# Count the number of heads and tails
heads_count = sum(observation)
tails_count = len(observation) - heads_count

# Priors
priors = [(2, 5), (5, 2), (1, 1), (2, 2)]

# Plot the posterior and prior distributions
x = np.linspace(0, 1, 1000)

for a, b in priors:
    posterior_a = a + heads_count
    posterior_b = b + tails_count

    # Calculate the prior and posterior distributions
    prior = beta.pdf(x, a, b)
    posterior = beta.pdf(x, posterior_a, posterior_b)

    # Create a new figure for each case
    plt.figure(figsize=(6, 4))

    # Plot the prior distribution
    plt.plot(x, prior, label=f'Prior: Beta({a}, {b})')

    # Plot the posterior distribution
    plt.plot(x, posterior, label=f'Posterior: Beta({posterior_a}, {posterior_b})')

    # Calculate MLE and MAP estimates
    mle = heads_count / len(observation)
    map_estimate = (posterior_a - 1) / (posterior_a + posterior_b - 2)

    # Plot MLE and MAP estimates
    plt.axvline(x=mle, color='black', linestyle='--', label=f'MLE ({mle:.2f})')
    plt.axvline(x=map_estimate, color='red', linestyle='--', label=f'MAP ({map_estimate:.2f})')

    plt.xlabel('Bias')
    plt.ylabel('Probability Density')
    plt.title(f'Prior and Posterior Distributions - Case: Beta({a}, {b})')
    plt.legend()
    plt.tight_layout()
    plt.show()