import numpy as np

weights = [0.5, 0.5]
components = [
    {'n': 6, 'alpha': 0.4, 'beta': 3.5},
    {'n': 6, 'alpha': 3.5, 'beta': 0.4}
]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    params = components[k]
    p = np.random.beta(params['alpha'], params['beta'])
    x = np.random.binomial(params['n'], p)
    samples.append(x)

print(samples)
