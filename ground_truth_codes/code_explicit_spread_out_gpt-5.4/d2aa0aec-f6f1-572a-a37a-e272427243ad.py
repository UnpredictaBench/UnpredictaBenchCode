import numpy as np

# Binomial distribution parameters
n = 100
p = 0.5

# List to store samples
samples = []

# Draw 1000 samples
for _ in range(10000):
    sample = np.random.binomial(n=n, p=p)
    samples.append(sample)

# Print the final list
print(samples)
