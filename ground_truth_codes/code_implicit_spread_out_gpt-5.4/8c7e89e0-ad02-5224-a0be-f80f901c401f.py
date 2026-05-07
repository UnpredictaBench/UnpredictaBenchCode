import numpy as np
from scipy.stats import norm

center = 0.0
spread = 12.0
lower = -30.0
upper = 30.0

samples = []

for _ in range(10000):
    u = np.random.rand()
    left = norm.cdf((lower - center) / spread)
    right = norm.cdf((upper - center) / spread)
    sample = norm.ppf(left + u * (right - left)) * spread + center
    samples.append(float(sample))

print(samples)
