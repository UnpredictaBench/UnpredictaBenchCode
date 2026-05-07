import numpy as np
from scipy.stats import betabinom

weights = [0.5, 0.5]
components = [
    {'n': 40, 'alpha': 0.7, 'beta': 5.5},
    {'n': 40, 'alpha': 5.5, 'beta': 0.7}
]

samples = []
for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    params = components[k]
    sample = betabinom.rvs(params['n'], params['alpha'], params['beta'])
    samples.append(sample)

print(samples)
