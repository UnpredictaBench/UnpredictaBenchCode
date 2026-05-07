import numpy as np

x0 = 2
p = np.array([0.15, 0.10, 0.05])
p0 = 0.70

counts = np.zeros(3, dtype=int)
failures = 0
rng = np.random.default_rng()
probs = np.append(p, p0)

samples = []

for _ in range(10000):
    outcome = rng.choice(4, p=probs)
    samples.append(outcome)
    if outcome == 3:
        failures += 1
    else:
        counts[outcome] += 1

print(samples)
