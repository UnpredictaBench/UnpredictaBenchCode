import numpy as np

rng = np.random.default_rng()
weights = np.array([0.58, 0.22, 0.12, 0.08])  # first entry is the stopping event
samples = []

for _ in range(10000):
    outcome = rng.choice(4, p=weights)
    samples.append(outcome)

print(samples)
