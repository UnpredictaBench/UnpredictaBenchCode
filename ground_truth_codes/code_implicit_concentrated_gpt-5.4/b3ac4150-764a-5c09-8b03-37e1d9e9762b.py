import numpy as np

rng = np.random.default_rng()
chances = np.array([0.08, 0.12, 0.10, 0.07, 0.09, 0.11])
outcomes = []

for _ in range(10000):
    outcome = rng.binomial(1, chances).sum()
    outcomes.append(int(outcome))

print(outcomes)
