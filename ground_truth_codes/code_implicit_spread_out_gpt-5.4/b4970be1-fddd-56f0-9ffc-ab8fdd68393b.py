import numpy as np

rng = np.random.default_rng()
trials = 36
weights = np.array([0.19, 0.17, 0.16, 0.14, 0.12, 0.11, 0.11])
results = []

for _ in range(10000):
    counts = rng.multinomial(trials, weights)
    result = int(np.dot(counts, np.arange(1, len(weights) + 1)))
    results.append(result)

print(results)
