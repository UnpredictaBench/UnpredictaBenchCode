import numpy as np

weights = [0.45, 0.55]
lambdas = [0.08, 1.6]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.exponential(scale=1 / lambdas[component])
    samples.append(sample)

print(samples)
