import numpy as np

# Multinomial distribution parameters
n = 30
p = [0.2, 0.2, 0.2, 0.2, 0.2]

# List to store samples
samples = []

# Draw samples in a loop
for _ in range(10000):
    sample = np.random.multinomial(n, p)
    samples.append(sample.tolist())  # Convert numpy array to list

# Flatten the list of lists into a single list of numbers
flattened_samples = [item for sublist in samples for item in sublist]

# Print the list of 1000 numbers
print(flattened_samples[:1000])
