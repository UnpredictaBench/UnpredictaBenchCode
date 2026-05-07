import numpy as np

x0 = 3
p1 = 0.12
p2 = 0.08
p0 = 0.80
probs = [p1, p2, p0]

samples = []
rng = np.random.default_rng()

for _ in range(10000):
    outcome = rng.choice(3, p=probs)
    samples.append(outcome)

print(samples)
