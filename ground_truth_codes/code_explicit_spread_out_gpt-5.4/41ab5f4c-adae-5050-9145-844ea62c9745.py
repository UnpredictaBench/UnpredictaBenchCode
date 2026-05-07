import numpy as np

# Parameters
sigma = 4.5
n = 3

# List to store sampled values
samples = []

# Loop to draw 1000 samples
for _ in range(10000):
    r = np.random.rayleigh(scale=sigma)
    x = np.random.normal(loc=r, scale=n)
    samples.append(x)

# Print the final list of samples
print(samples)
