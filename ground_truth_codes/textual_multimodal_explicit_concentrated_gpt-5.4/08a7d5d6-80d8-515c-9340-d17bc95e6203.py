import numpy as np

lambdas = [1, 4]
weights = [0.5, 0.5]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    sample = np.random.poisson(lambdas[chosen])
    samples.append(sample)

print(samples)
