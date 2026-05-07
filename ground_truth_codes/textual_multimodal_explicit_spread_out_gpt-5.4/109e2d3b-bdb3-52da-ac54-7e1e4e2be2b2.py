import numpy as np

weights = np.array([0.5, 0.5])
alphas = [
    np.array([0.2, 0.2, 0.2, 0.2]),
    np.array([8.0, 0.2, 0.2, 0.2])
]

samples = []
for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.dirichlet(alphas[component])
    samples.append(float(sample[0]))

print(samples)
