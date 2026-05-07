import numpy as np

p = np.array([0.04, 0.05, 0.03, 0.06, 0.04, 0.05])
samples = []

for _ in range(10000):
    bernoulli_trial = np.random.binomial(1, p)
    sample = int(bernoulli_trial.sum())
    samples.append(sample)

print(samples)
