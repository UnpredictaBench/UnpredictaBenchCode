import numpy as np
from scipy.stats import t

weights = [0.5, 0.5]
locations = [-1.2, 1.2]
scales = [0.25, 0.25]
dfs = [8, 8]

samples = []
for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    sample = t.rvs(df=dfs[k], loc=locations[k], scale=scales[k])
    samples.append(float(sample))

print(samples)
