import numpy as np
from scipy.stats import chi2

mu = np.array([12.0, -8.0, 5.0])
Sigma = np.array([
    [9.0, 4.5, -2.0],
    [4.5, 16.0, 3.0],
    [-2.0, 3.0, 25.0]
])
nu = 2.7

samples = []

for _ in range(10000):
    u_sample = chi2.rvs(df=nu)
    y = np.random.multivariate_normal(mean=np.zeros(3), cov=Sigma)
    x = y * np.sqrt(nu / u_sample) + mu
    sample = float(x[1])
    samples.append(sample)

print(samples)
