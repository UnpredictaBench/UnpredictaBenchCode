import numpy as np

rng = np.random.default_rng()
base_level = 250.0
spread = 35.0
samples = []

for _ in range(10000):
    u = rng.uniform(1e-12, 1 - 1e-12)
    sample = base_level - spread * np.log(-np.log(u))
    samples.append(float(sample))

print(samples)
