import numpy as np

# Parameters for the inverse Gaussian (Wald) distribution
mu = 1.0
lam = 20.0

samples = []

for _ in range(10000):
    # Michael-Schucany-Haas sampling algorithm for IG(mu, lambda)
    v = np.random.normal(0.0, 1.0)
    y = v**2
    x = mu + (mu**2 * y) / (2.0 * lam) - (mu / (2.0 * lam)) * np.sqrt(4.0 * mu * lam * y + mu**2 * y**2)
    z = np.random.uniform(0.0, 1.0)

    sample = x if z <= mu / (mu + x) else (mu**2) / x
    samples.append(float(sample))

print(samples)
