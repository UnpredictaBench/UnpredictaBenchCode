import numpy as np

weights = [0.5, 0.5]
components = [
    {'n': 4, 'p': [0.88, 0.08, 0.04]},
    {'n': 4, 'p': [0.04, 0.08, 0.88]}
]

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    sample = np.random.multinomial(components[chosen]['n'], components[chosen]['p'])
    samples.append(int(sample[0]))

print(samples)
