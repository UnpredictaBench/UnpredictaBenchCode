import numpy as np

rng = np.random.default_rng()
center = np.array([8.0, -11.0, 5.5])
spread = np.array([
    [16.0, 5.0, 2.0],
    [5.0, 25.0, -4.0],
    [2.0, -4.0, 9.0]
])
df = 2.5

samples = []
for _ in range(10000):
    z = rng.multivariate_normal(mean=np.zeros(3), cov=spread)
    u = rng.chisquare(df)
    point = center + z * np.sqrt(df / u)
    samples.append(float(point[0]))

print(samples)
