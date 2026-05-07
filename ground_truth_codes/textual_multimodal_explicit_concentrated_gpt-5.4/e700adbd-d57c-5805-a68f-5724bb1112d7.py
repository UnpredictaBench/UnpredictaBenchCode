import numpy as np

weights = [0.55, 0.45]
components = [
    {'alpha': 8.0, 'scale': 0.18, 'location': 0.9},
    {'alpha': 9.0, 'scale': 0.16, 'location': 1.55}
]

samples = []

for _ in range(10000):
    j = np.random.choice([0, 1], p=weights)
    u = np.random.uniform()
    a = components[j]['alpha']
    s = components[j]['scale']
    m = components[j]['location']
    sample = m + s * (-np.log(u))**(-1.0 / a)
    samples.append(float(sample))  # Convert to float to ensure valid Python literal

print(samples)
