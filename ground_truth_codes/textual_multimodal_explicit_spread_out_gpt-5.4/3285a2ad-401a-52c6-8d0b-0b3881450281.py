import numpy as np

weights = [0.45, 0.55]
components = [(-18, 7), (24, 11)]  # (mu, beta)
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    mu, beta = components[chosen]
    u = np.random.uniform(0.0, 1.0)
    sample = mu - beta * np.log(-np.log(u))
    samples.append(float(sample))  # Convert to float to avoid np.float64

print(samples)
