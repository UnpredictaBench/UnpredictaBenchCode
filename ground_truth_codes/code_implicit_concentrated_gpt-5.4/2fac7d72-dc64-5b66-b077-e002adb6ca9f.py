import numpy as np

target_level = 1.2
drift_rate = 2.0
noise_scale = 0.3

mu = target_level / drift_rate
lam = (target_level / noise_scale) ** 2

samples = []

for _ in range(10000):
    v = np.random.normal()
    y = v * v
    x = mu + (mu * mu * y) / (2 * lam) - (mu / (2 * lam)) * np.sqrt(4 * mu * lam * y + mu * mu * y * y)
    
    u = np.random.uniform()
    sample = x if u <= mu / (mu + x) else (mu * mu) / x
    samples.append(float(sample))

print(samples)
