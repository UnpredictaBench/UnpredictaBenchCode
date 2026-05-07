import numpy as np

rng = np.random.default_rng()
center = np.array([0.08, -0.04])
shape = np.array([[0.06, 0.01], [0.01, 0.05]])
df = 12.0

samples = []

for _ in range(10000):
    z = rng.multivariate_normal(mean=np.zeros(2), cov=shape)
    u = rng.chisquare(df)
    point = center + z * np.sqrt(df / u)
    sample = point[0]
    samples.append(float(sample))

print(samples)
