import numpy as np

low = 4.8
high = 5.2
samples = []

for _ in range(10000):
    reading = low + (high - low) * np.random.random()
    samples.append(reading)

print(samples)
