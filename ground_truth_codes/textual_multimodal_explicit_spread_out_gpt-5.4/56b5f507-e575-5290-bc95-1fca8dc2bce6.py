import numpy as np

weights = np.array([0.5, 0.5])
mus = [np.array([-18.0, 12.0]), np.array([22.0, -15.0])]
Sigmas = [np.array([[25.0, 8.0], [8.0, 16.0]]), np.array([[36.0, -10.0], [-10.0, 25.0]])]
nus = [3.0, 4.0]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    u = np.random.chisquare(df=nus[k])
    y = np.random.multivariate_normal(mean=np.zeros(2), cov=Sigmas[k])
    x = mus[k] + y * np.sqrt(nus[k] / u)
    samples.append(float(x[0]))

print(samples)
