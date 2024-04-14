import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig = plt.figure()
fig.set_size_inches(18.5, 10.5)
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

def prob_ratio(n, k, num):
    if n <= k + 1:
        return np.nan
    doors = ['C' for _ in range(k)]
    doors += ['G' for _ in range(n-k)]

    win_og = 0
    win_sw = 0
    choices = np.arange(0,n)
    host_choices = np.arange(k,n)
    for _ in range(num):
        choices_curr = choices.copy()
        host_choices_curr = host_choices.copy()
        choice = np.random.choice(choices_curr)
        if doors[choice] == 'C':
            win_og += 1
        else : #chosen gate has a goat, so host has to pick a gate other than this gate
            host_choices_curr = np.delete(host_choices, np.where(host_choices == choice))
        # if choice == n - 1 :
        #     choice = n - 2
        host_choice = np.random.choice(host_choices_curr)
        choices_curr = np.delete(choices_curr, np.where(choices_curr == choice))
        choices_curr = np.delete(choices_curr, np.where(choices_curr == host_choice))
        new_choice = np.random.choice(choices_curr)
        # while new_choice == choice:
        #     new_choice = np.random.randint(0, n - 1)
        if doors[new_choice] == 'C':
            win_sw += 1
        
    prob_og = float(win_og) / num
    prob_sw = float(win_sw) / num

    return prob_sw / prob_og

def prob_ratio_exact(n, k):
    if n <= k + 1:
        return np.nan
    else:
        return (n - 1)/(n - 2)

# Make data for the first surface.
N = 100
num = 1000
n = np.arange(3, N, 1)
k = np.arange(1, N - 2, 1)
n, k = np.meshgrid(n, k)
vectorized_prob_ratio = np.vectorize(prob_ratio)
vectorized_prob_ratio_exact = np.vectorize(prob_ratio_exact)
Z = vectorized_prob_ratio(n, k, num)

# Plot the first surface.
surf = ax1.plot_surface(n, k, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax1.set_title('Plot from Simulation')

# Make data for the second surface (initially set to a plane).
Z_exact = vectorized_prob_ratio_exact(n, k)

# Plot the second surface (plane).
surf_plane = ax2.plot_surface(n, k, Z_exact,cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax2.set_title('Plot from Exact Calculation')


# Set the same color map for both plots
surf.set_cmap(cm.coolwarm)
surf_plane.set_cmap(cm.coolwarm)
# Customize the z axis.
ax1.set_zlim(0.5, 2.5)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter('{x:.02f}')
ax1.set_xlabel("n")
ax1.set_ylabel("k")
ax1.set_zlabel('P_W/P_T')

ax2.set_zlim(0.5, 2.5)
ax2.zaxis.set_major_locator(LinearLocator(10))
ax2.zaxis.set_major_formatter('{x:.02f}')
ax2.set_xlabel("n")
ax2.set_ylabel("k")
ax2.set_zlabel('P_W/P_T')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.savefig("finalplot.png")
plt.show()
