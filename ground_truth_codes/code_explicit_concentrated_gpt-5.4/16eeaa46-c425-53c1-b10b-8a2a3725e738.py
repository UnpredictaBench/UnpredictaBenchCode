import numpy as np

# Weibull distribution parameters
lambda_scale = 0.8
k_shape = 6.0

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = lambda_scale * (-np.log(1.0 - u))**(1.0 / k_shape)
    samples.append(float(sample))

print(samples)
