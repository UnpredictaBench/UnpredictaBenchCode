import numpy as np

center = -12.7
spread = 9.4
samples = []

for _ in range(10000):
    reading = center + spread * np.random.standard_normal()
    samples.append(float(reading))

print(samples)
