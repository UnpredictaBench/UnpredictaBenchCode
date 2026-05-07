import numpy as np

rng = np.random.default_rng()
base_level = 3.8
noise_scale = 6.4
outcomes = []

for _ in range(10000):
    raw = rng.normal(loc=base_level, scale=noise_scale)
    outcome = max(0.0, raw)
    outcomes.append(outcome)

print(outcomes)
