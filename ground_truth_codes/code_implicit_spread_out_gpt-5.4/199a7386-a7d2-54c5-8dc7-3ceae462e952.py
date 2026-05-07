import random

start = -480
end = 520
samples = []

for _ in range(10000):
    sample = random.randint(start, end)
    samples.append(sample)

print(samples)
