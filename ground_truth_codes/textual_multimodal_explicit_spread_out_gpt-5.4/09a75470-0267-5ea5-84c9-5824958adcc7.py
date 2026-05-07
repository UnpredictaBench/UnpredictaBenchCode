import numpy as np

weights = [0.4, 0.6]
scales = [1.5, 18.0]
shapes = [0.8, 3.5]

samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = scales[component] * (-np.log(1 - np.random.uniform())) ** (1 / shapes[component])
    samples.append(float(sample))

print(samples)
