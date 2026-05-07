import numpy as np

mu = np.array([0.0, -5.0, 8.0])
Sigma = np.array([
    [9.0,  4.5, -2.0],
    [4.5, 16.0,  3.5],
    [-2.0, 3.5, 25.0]
])
nu = 2.5

rng = np.random.default_rng(123)

values = []

for _ in range(10000):
    y = rng.multivariate_normal(mean=np.zeros(len(mu)), cov=Sigma)
    u = rng.chisquare(df=nu)
    x = mu + y * np.sqrt(nu / u)
    values.append(x[0])

print(values)