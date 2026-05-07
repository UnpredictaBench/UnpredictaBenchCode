import numpy as np

weights = [0.45, 0.55]
components = [
    {'alpha': 0.9, 's': 3.5, 'm': 0.0},
    {'alpha': 1.4, 's': 18.0, 'm': 30.0}
]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    u = np.random.uniform()
    alpha = components[k]['alpha']
    s = components[k]['s']
    m = components[k]['m']
    sample = m + s * (-np.log(u)) ** (-1.0 / alpha)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
