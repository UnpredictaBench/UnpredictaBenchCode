import numpy as np
from scipy.stats import hypergeom

weights = [0.5, 0.5]
components = [
    {'N': 120, 'K': 18, 'n': 40},
    {'N': 120, 'K': 92, 'n': 40}
]

samples = []
for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    params = components[chosen]
    sample = hypergeom.rvs(M=params['N'], n=params['K'], N=params['n'])
    samples.append(int(sample))

print(samples)
