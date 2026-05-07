import numpy as np

weights = [0.5, 0.5]
p1 = np.array([0.02, 0.05, 0.08, 0.10, 0.12, 0.15, 0.18, 0.20, 0.22, 0.25, 0.28, 0.30])
p2 = np.array([0.70, 0.72, 0.75, 0.78, 0.80, 0.82, 0.85, 0.88, 0.90, 0.92, 0.95, 0.98])

samples = []
for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    p = p1 if component == 0 else p2
    sample = np.random.binomial(1, p).sum()
    samples.append(int(sample))

print(samples)
