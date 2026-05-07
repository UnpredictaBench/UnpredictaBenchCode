import numpy as np

center = -1.8
width = 6.4
readings = []

for _ in range(10000):
    left_push = np.random.exponential(scale=width)
    right_push = np.random.exponential(scale=width)
    reading = center + (left_push - right_push)
    readings.append(float(reading))

print(readings)
