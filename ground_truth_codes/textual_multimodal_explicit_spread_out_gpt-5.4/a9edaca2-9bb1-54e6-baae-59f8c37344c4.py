import numpy as np

weights = [0.5, 0.5]
lambdas = [3, 18]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.poisson(lambdas[component])
    samples.append(sample)

print(samples)
