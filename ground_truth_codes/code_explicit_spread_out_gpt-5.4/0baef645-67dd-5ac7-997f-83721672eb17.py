import numpy as np
from scipy.stats import t

# Parameters
nu = 1.2  # degrees of freedom (> 0), chosen small for heavy tails

# List to store samples
samples = []

# Draw 1000 random samples from Student's t distribution
for _ in range(10000):
    sample = t.rvs(df=nu)
    samples.append(float(sample))  # Convert np.float64 to float

# Print the final list of samples
print(samples)
