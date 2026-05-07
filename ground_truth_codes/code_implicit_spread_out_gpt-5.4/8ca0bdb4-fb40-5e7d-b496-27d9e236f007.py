import numpy as np

scale = 18.7
shape = 0.58
samples = []

for _ in range(10000):
    u = np.random.uniform()
    sample = scale * (-np.log(1 - u))**(1 / shape)
    samples.append(float(sample))

print(samples)
