import random

low = 2
high = 4
samples = []

for _ in range(10000):
    pick = random.randint(low, high)
    samples.append(pick)

print(samples)
