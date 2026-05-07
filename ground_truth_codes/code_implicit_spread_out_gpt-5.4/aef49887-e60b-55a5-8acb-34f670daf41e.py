import numpy as np

center = np.array([12.0, -8.0, 5.0, 20.0])
spread = np.array([
    [9.0, 4.2, -1.5, 2.0],
    [4.2, 16.0, 3.6, -2.4],
    [-1.5, 3.6, 25.0, 5.5],
    [2.0, -2.4, 5.5, 36.0]
])
L = np.linalg.cholesky(spread)

results = []
for _ in range(10000):
    base = np.random.standard_normal(4)
    point = center + L @ base
    result = point[0] - 0.5 * point[1] + 0.25 * point[2] + point[3]
    results.append(float(result))

print(results)
