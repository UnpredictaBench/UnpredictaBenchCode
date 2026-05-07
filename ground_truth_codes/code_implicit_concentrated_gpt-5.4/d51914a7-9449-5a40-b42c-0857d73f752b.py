import numpy as np

scale = 0.9
shape = 8.0
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = scale * (-np.log(1.0 - u))**(1.0 / shape)
    samples.append(float(sample))

print(samples)
