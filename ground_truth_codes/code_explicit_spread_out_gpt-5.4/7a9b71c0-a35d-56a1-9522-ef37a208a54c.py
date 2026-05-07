import numpy as np

# Inverse Gaussian (Wald) distribution parameters
mu = 8.0
lam = 0.8

samples = []

for _ in range(10000):
    # Michael-Schucany-Haas method for sampling IG(mu, lam)
    v = np.random.normal(0.0, 1.0)
    y = v**2
    x = mu + (mu**2 * y) / (2 * lam) - (mu / (2 * lam)) * np.sqrt(4 * mu * lam * y + mu**2 * y**2)
    z = np.random.uniform(0.0, 1.0)

    sample = x if z <= mu / (mu + x) else (mu**2) / x
    samples.append(float(sample))

print(samples)
