import numpy as np
from scipy.stats import chi2

mu = np.array([0.0, 0.0])
Sigma = np.array([[0.04, 0.0], [0.0, 0.04]])
nu = 20

samples = []

for _ in range(10000):
    y = np.random.multivariate_normal(mean=[0.0, 0.0], cov=Sigma)
    u_sample = chi2.rvs(df=nu)
    x = mu + y * np.sqrt(nu / u_sample)
    samples.append(float(x[0]))

print(samples)
