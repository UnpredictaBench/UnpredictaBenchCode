import numpy as np

# Compound Poisson parameters
lam = 1.2          # Poisson rate
jump_low = 0.2     # lower bound for jump sizes
jump_high = 0.8    # upper bound for jump sizes

samples = []

for _ in range(10000):
    # Sample the number of jumps
    N = np.random.poisson(lam)
    
    # Sample the jump sizes and sum them
    if N == 0:
        sample = 0.0
    else:
        jumps = np.random.uniform(jump_low, jump_high, size=N)
        sample = float(np.sum(jumps))
    
    samples.append(sample)

print(samples)
