import numpy as np

trials = 120
chance = 0.5
outcomes = []

for _ in range(10000):
    outcome = np.random.default_rng().binomial(trials, chance)
    outcomes.append(outcome)

print(outcomes)
