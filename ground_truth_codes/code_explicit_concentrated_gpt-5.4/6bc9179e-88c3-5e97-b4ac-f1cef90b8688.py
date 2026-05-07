import numpy as np

# Erlang distribution parameters
k = 2          # positive integer shape
lam = 5.0      # positive rate

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0, size=k)
    sample = -(1.0 / lam) * np.log(u).sum()
    samples.append(float(sample))

print(samples)
