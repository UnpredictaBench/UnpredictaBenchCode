import numpy as np

# Success probabilities for 5 independent Bernoulli trials
p = np.array([0.05, 0.08, 0.10, 0.12, 0.07])

# List to store samples
samples = []

# Draw one sample at a time in a loop
for _ in range(10000):
    # Draw independent Bernoulli outcomes and sum the successes
    sample = np.random.binomial(1, p).sum()
    samples.append(int(sample))  # Convert np.int64 to int

# Print the final list of samples
print(samples)
