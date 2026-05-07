import numpy as np

# Categorical distribution over 8 categories
k = 8
p = np.array([0.12, 0.13, 0.11, 0.14, 0.10, 0.15, 0.13, 0.12])

# Validate probabilities
assert len(p) == k
assert np.all(p >= 0)
assert np.isclose(p.sum(), 1.0)

# Draw samples in a loop
categories = np.arange(1, k + 1)
samples = []

for _ in range(10000):
    sample = np.random.choice(categories, p=p)
    samples.append(int(sample))  # Convert np.int64 to int

print(samples)
