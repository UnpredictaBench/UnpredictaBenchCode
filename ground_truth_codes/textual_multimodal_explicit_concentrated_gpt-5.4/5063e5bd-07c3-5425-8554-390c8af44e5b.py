import numpy as np

weights = [0.5, 0.5]
params = [(2, 0.85), (2, 0.35)]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    r, p = params[component]
    sample = np.random.negative_binomial(r, p)
    samples.append(int(sample))

print(samples)
