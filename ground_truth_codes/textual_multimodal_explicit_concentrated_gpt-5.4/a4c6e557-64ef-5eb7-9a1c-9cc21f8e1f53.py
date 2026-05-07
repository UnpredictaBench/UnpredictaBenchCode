import numpy as np

mixture_weights = [0.5, 0.5]
components = [
    [0.9, 0.08, 0.02],
    [0.02, 0.08, 0.9]
]
categories = np.array([1, 2, 3])

samples = []

for _ in range(10000):
    chosen_component = np.random.choice([0, 1], p=mixture_weights)
    sample = np.random.choice(categories, p=components[chosen_component])
    samples.append(int(sample))  # Convert np.int64 to int

print(samples)
