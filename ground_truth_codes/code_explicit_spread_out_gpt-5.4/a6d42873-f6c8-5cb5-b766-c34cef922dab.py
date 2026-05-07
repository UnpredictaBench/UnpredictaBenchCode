import numpy as np

# Weibull distribution parameters
lambda_scale = 8.0
k_shape = 0.6

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = lambda_scale * (-np.log(1.0 - u))**(1.0 / k_shape)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
