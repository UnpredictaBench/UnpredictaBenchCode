import numpy as np

left = 4.8
right = 5.1
peak = 4.92
samples = []

for _ in range(10000):
    u = np.random.uniform()
    cut = (peak - left) / (right - left)

    if u < cut:
        sample = left + np.sqrt(u * (right - left) * (peak - left))
    else:
        sample = right - np.sqrt((1 - u) * (right - left) * (right - peak))
    
    samples.append(float(sample))

print(samples)
