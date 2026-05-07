import numpy as np
from scipy.stats import truncnorm

weights = [0.5, 0.5]

params = [
    {'mean': -18, 'std': 9, 'lower': -35, 'upper': -2},
    {'mean': 22, 'std': 11, 'lower': 5, 'upper': 45}
]

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    p = params[chosen]
    a = (p['lower'] - p['mean']) / p['std']
    b = (p['upper'] - p['mean']) / p['std']
    sample = truncnorm.rvs(a, b, loc=p['mean'], scale=p['std'])
    samples.append(float(sample))

print(samples)
