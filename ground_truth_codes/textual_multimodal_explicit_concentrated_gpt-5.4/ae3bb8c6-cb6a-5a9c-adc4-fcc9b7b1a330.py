import numpy as np
from scipy.stats import hypergeom

weights = [0.5, 0.5]
components = [
    {'N': 18, 'K': 2, 'n': 2},
    {'N': 18, 'K': 16, 'n': 2}
]

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    params = components[chosen]
    sample = hypergeom.rvs(M=params['N'], n=params['K'], N=params['n'])
    samples.append(sample)

print(samples)
