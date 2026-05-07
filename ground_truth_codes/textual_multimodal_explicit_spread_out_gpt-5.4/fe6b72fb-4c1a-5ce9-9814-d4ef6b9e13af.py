import numpy as np
from scipy.stats import t

weights = [0.5, 0.5]
components = [
    {'df': 2.5, 'loc': -18, 'scale': 9},
    {'df': 3.2, 'loc': 24, 'scale': 11}
]

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    params = components[chosen]
    sample = t.rvs(df=params['df'], loc=params['loc'], scale=params['scale'])
    samples.append(float(sample))

print(samples)
