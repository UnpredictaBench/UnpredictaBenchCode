import numpy as np

baseline = 0.18
jitter = 0.04
samples = []

for _ in range(10000):
    reading = baseline + jitter * np.random.standard_normal()
    samples.append(float(reading))

print(samples)
