import numpy as np
from scipy.stats import chi2

mu = np.array([0.1, -0.05])
Sigma = np.array([[0.18, 0.04], [0.04, 0.12]])
nu = 9

samples = []
for _ in range(10000):
    y = np.random.multivariate_normal(mean=np.zeros(2), cov=Sigma)
    u_draw = chi2.rvs(df=nu)
    x = mu + y * np.sqrt(nu / u_draw)
    samples.append(float(x[0]))

print(samples)
