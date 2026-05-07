import numpy as np

# Parameters for a 2D multivariate t-distribution
mu = np.array([0.0, 0.0])
Sigma = np.array([[0.2, 0.05],
                  [0.05, 0.15]])
nu = 10.0

samples = []

for _ in range(10000):
    y = np.random.multivariate_normal(mean=np.zeros(2), cov=Sigma)
    u_chi = np.random.chisquare(df=nu)
    x = mu + y * np.sqrt(nu / u_chi)
    samples.append(float(x[0]))

print(samples)
