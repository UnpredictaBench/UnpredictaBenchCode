import numpy as np

n = 12
p = [0.82, 0.10, 0.06, 0.02]
scrap_counts = []

for _ in range(10000):
    sample = np.random.multinomial(n, p)
    scrap_count = int(sample[3])  # Convert np.int64 to int
    scrap_counts.append(scrap_count)

print(scrap_counts)
