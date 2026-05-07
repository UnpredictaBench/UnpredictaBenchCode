import numpy as np

# Poisson binomial parameters: independent Bernoulli success probabilities
p = np.array([0.08, 0.17, 0.26, 0.34, 0.43, 0.52, 0.61, 0.69, 0.78, 0.91])

samples = []

for _ in range(10000):
    bernoulli_trials = np.random.binomial(1, p)
    sample = int(np.sum(bernoulli_trials))
    samples.append(sample)

print(samples)
