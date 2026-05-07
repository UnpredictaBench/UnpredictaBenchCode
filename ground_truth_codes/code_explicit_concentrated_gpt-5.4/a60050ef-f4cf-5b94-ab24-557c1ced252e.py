import numpy as np

# Multinomial distribution parameters
n = 12
p = [0.85, 0.10, 0.05]

# List to store samples
samples = []

# Draw samples in a loop
for _ in range(10000):
    sample = np.random.multinomial(n=n, pvals=p)
    samples.append(int(sample[0]))  # Convert np.int64 to int

# Print the final list
print(samples)
