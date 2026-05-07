import numpy as np

weights = [0.55, 0.45]
scales = [0.9, 1.8]
shapes = [3.5, 4.0]

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    sample = scales[chosen] * (-np.log(1 - np.random.rand()))**(1 / shapes[chosen])
    samples.append(float(sample))

print(samples)
