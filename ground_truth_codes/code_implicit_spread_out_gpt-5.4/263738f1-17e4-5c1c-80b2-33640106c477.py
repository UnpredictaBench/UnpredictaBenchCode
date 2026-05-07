import numpy as np

rng = np.random.default_rng()
chances = np.array([0.08, 0.14, 0.19, 0.27, 0.33, 0.41, 0.48, 0.52, 0.59, 0.67, 0.73, 0.81, 0.88])
outcomes = []

for _ in range(10000):
    sample = rng.binomial(1, chances).sum()
    outcomes.append(int(sample))

print(outcomes)
