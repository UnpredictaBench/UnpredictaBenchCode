import numpy as np

# Dirichlet parameters
alpha = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# List to store sampled values
samples = []

# Loop to draw samples
for _ in range(10000):
    gamma_draws = np.random.gamma(shape=alpha, scale=1.0)
    sample = gamma_draws / gamma_draws.sum()
    samples.append(float(sample[0]))

# Print the final list
print(samples)
