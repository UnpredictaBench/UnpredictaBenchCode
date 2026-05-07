import numpy as np

weights = [0.5, 0.5]
components = [
    {'left': -30, 'mode': -20, 'right': 10},
    {'left': 20, 'mode': 55, 'right': 70}
]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    p = components[k]
    sample = np.random.triangular(p['left'], p['mode'], p['right'])
    samples.append(sample)

print(samples)
