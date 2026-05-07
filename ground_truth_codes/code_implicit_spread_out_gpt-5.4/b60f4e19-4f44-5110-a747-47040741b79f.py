import numpy as np

rng = np.random.default_rng()
p_success = 0.5
samples = []

for _ in range(10000):
    sample = rng.binomial(n=1, p=p_success)
    samples.append(sample)

print(samples)
