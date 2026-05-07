import numpy as np

# Beta distribution parameters
alpha = 1.0
beta = 1.0

# List to store samples
samples = []

# Draw 1000 random samples, one at a time
for _ in range(10000):
    sample = np.random.beta(alpha, beta)
    samples.append(sample)

# Print the final list of samples
print(samples)
