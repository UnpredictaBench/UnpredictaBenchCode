import numpy as np

floor = 0.8
heaviness = 0.55
samples = []

for _ in range(10000):
    u = np.random.random()
    sample = floor / (u ** (1.0 / heaviness))
    samples.append(float(sample))

print(samples)
