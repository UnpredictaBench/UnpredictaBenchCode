import numpy as np

trials = 30
shape1 = 0.7
shape2 = 0.6
outcomes = []

for _ in range(10000):
    rng = np.random.default_rng()
    chance = rng.beta(shape1, shape2)
    outcome = rng.binomial(trials, chance)
    outcomes.append(outcome)

print(outcomes)
