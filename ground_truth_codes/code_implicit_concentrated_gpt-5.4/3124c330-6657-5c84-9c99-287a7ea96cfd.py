import numpy as np

trials = 18
weights = np.array([0.82, 0.10, 0.05, 0.03])
samples = []

for _ in range(10000):
    rng = np.random.default_rng()
    counts = rng.multinomial(trials, weights)
    value = int(counts[0])
    samples.append(value)

print(samples)
