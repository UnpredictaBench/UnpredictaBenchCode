import numpy as np

# Fréchet distribution parameters
alpha = 0.65   # shape > 0
s = 12.0       # scale > 0
m = -8.0       # location

# List to store samples
samples = []

# Inverse-CDF sampling: X = m + s * (-ln U)^(-1/alpha), U ~ Uniform(0,1)
for _ in range(10000):
    U = np.random.uniform(0.0, 1.0)
    sample = m + s * (-np.log(U)) ** (-1.0 / alpha)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
