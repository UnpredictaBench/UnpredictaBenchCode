import numpy as np

# Categorical distribution over 4 categories labeled 1, 2, 3, 4
p = np.array([0.88, 0.08, 0.03, 0.01], dtype=float)
categories = np.array([1, 2, 3, 4])

# Validate probabilities
assert np.all(p >= 0), 'Probabilities must be nonnegative.'
assert np.isclose(p.sum(), 1.0), 'Probabilities must sum to 1.'

samples = []
for _ in range(10000):
    sample = np.random.choice(categories, p=p)
    samples.append(int(sample))  # Convert np.int64 to int

print(samples)
