import numpy as np
from scipy.stats import chi2

mu = np.array([0.0, -3.5, 5.0, 2.0])
Sigma = np.array([
    [9.0, 2.5, -1.0, 0.5],
    [2.5, 7.0, 1.5, -0.8],
    [-1.0, 1.5, 6.5, 2.0],
    [0.5, -0.8, 2.0, 8.0]
])
nu = 2.5

samples = []
for _ in range(10000):
    rng = np.random.default_rng()
    y = rng.multivariate_normal(mean=np.zeros(4), cov=Sigma)
    u = chi2.rvs(df=nu)
    x = mu + y * np.sqrt(nu / u)
    samples.append(float(x[0]))  # Convert np.float64 to float

print(samples)
