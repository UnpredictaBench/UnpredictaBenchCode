import numpy as np

rng = np.random.default_rng()
a = 180.0
b = 220.0
outcomes = []

for _ in range(10000):
    u = rng.gamma(shape=a, scale=1.0)
    v = rng.gamma(shape=b, scale=1.0)
    outcome = u / (u + v)
    outcomes.append(float(outcome))

print(outcomes)
