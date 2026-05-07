import numpy as np

weights = [0.5, 0.5]
components = [
    {'n': 24, 'p': [0.7, 0.1, 0.1, 0.1]},
    {'n': 24, 'p': [0.1, 0.1, 0.1, 0.7]}
]

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    sample = np.random.multinomial(components[chosen]['n'], components[chosen]['p'])
    samples.append(int(sample[0]))

print(samples)
