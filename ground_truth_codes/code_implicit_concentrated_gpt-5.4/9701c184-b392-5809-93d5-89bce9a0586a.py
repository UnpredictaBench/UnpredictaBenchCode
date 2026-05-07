import numpy as np
from scipy.stats import norm

center = 0.15
spread = 0.08
lower = 0.0
upper = 0.3

lo_cdf = norm.cdf((lower - center) / spread)
hi_cdf = norm.cdf((upper - center) / spread)

samples = []

for _ in range(10000):
    u = np.random.rand()
    value = norm.ppf(lo_cdf + u * (hi_cdf - lo_cdf)) * spread + center
    samples.append(float(value))

print(samples)
