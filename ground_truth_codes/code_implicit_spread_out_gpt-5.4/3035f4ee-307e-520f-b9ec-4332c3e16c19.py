import numpy as np

rng = np.random.default_rng()
rate_a = 24.0
rate_b = 17.0
outcomes = []

for _ in range(10000):
    arrivals_a = rng.poisson(rate_a)
    arrivals_b = rng.poisson(rate_b)
    outcome = arrivals_a - arrivals_b
    outcomes.append(outcome)

print(outcomes)
