import numpy as np

baseline = -0.18
noise = 0.09
values = []

for _ in range(10000):
    raw = np.random.normal(loc=baseline, scale=noise)
    value = max(0.0, raw)
    values.append(value)

print(values)
