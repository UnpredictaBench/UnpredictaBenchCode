import numpy as np

left_shape = 0.6
right_shape = 0.6
outcomes = []

for _ in range(10000):
    rng = np.random.default_rng()
    x = rng.gamma(shape=left_shape, scale=1.0)
    y = rng.gamma(shape=right_shape, scale=1.0)
    outcome = x / (x + y)
    outcomes.append(float(outcome))

print(outcomes)
