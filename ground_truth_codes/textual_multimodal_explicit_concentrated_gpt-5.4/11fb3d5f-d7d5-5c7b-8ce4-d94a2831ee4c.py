import numpy as np

weights = np.array([0.5, 0.5])
alphas = [np.array([18, 2, 2]), np.array([2, 18, 2])]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.dirichlet(alphas[component])
    samples.append(float(sample[0]))  # Convert np.float64 to float

print(samples)
