import numpy as np

# Dirichlet parameters chosen to make samples relatively concentrated
alpha = np.array([25.0, 25.0, 25.0, 25.0])

# List to store the samples
samples = []

# Draw one sample at a time inside a loop that runs 1000 iterations
for _ in range(10000):
    sample = np.random.dirichlet(alpha)
    samples.append(float(sample[0]))

# Print the final list
print(samples)
