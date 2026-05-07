import numpy as np

weights = [0.5, 0.5]
components = [
    {'a': 0.0, 'b': 0.3, 'c': 0.08},
    {'a': 0.55, 'b': 0.85, 'c': 0.73}
]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    a = components[k]['a']
    b = components[k]['b']
    c = components[k]['c']

    u = np.random.rand()
    fc = (c - a) / (b - a)
    if u < fc:
        sample = a + np.sqrt(u * (b - a) * (c - a))
    else:
        sample = b - np.sqrt((1 - u) * (b - a) * (b - c))
    
    samples.append(float(sample))

print(samples)
