import numpy as np

low = -980.0
high = 1240.0
samples = []

for _ in range(10000):
    reading = low + (high - low) * np.random.random()
    samples.append(reading)

print(samples)
