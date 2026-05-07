import numpy as np
from scipy.stats import t

nu = 30
samples = []

for _ in range(10000):
    sample = t.rvs(df=nu)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
