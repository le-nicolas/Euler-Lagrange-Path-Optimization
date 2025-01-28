import numpy as np
import matplotlib.pyplot as plt

# Define start and end points
t1, y1 = 0, 0  # Point A
t2, y2 = 100, 5  # Point B

# Time range
t = np.linspace(t1, t2, 100)

# Generate random non-optimal paths
num_random_paths = 10
random_paths = []
for _ in range(num_random_paths):
    noise = np.cumsum(np.random.randn(len(t)) * 0.2)  # Cumulative random walk
    random_paths.append(np.linspace(y1, y2, len(t)) + noise)

# Compute the optimal path (straight line between A and B)
optimal_path = np.linspace(y1, y2, len(t))

# Plotting
plt.figure(figsize=(10, 5), facecolor='black')
plt.gca().set_facecolor("black")

# Plot random paths
for path in random_paths:
    path[-1] = y2  # Ensure all random paths lead to B
    plt.plot(t, path, alpha=0.6, linewidth=1, linestyle='-', color=np.random.rand(3,))

# Plot optimal path
plt.plot(t, optimal_path, 'w-', linewidth=3, label='Optimal Path')

# Mark points A and B
plt.scatter([t1, t2], [y1, y2], color='white', s=100)
plt.text(t1, y1, 'A', fontsize=15, color='white', verticalalignment='bottom', horizontalalignment='right')
plt.text(t2, y2, 'B', fontsize=15, color='white', verticalalignment='bottom', horizontalalignment='left')

plt.xlabel("Time (t)", color='white')
plt.ylabel("Position (y)", color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.legend()
plt.show()
