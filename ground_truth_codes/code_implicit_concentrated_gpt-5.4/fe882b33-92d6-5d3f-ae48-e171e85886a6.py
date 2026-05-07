import numpy as np

rng = np.random.default_rng()
df = 30
samples = []

for _ in range(10000):
    z = rng.normal(0.0, 1.0)
    v = rng.chisquare(df)
    outcome = z / np.sqrt(v / df)
    samples.append(float(outcome))

print(samples)
