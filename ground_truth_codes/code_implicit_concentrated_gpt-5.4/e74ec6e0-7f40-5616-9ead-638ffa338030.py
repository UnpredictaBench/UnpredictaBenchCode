import numpy as np

rng = np.random.default_rng()
trials = 8
shape1 = 40.0
shape2 = 60.0
results = []

for _ in range(10000):
    hidden_rate = rng.beta(shape1, shape2)
    result = rng.binomial(trials, hidden_rate)
    results.append(int(result))

print(results)
