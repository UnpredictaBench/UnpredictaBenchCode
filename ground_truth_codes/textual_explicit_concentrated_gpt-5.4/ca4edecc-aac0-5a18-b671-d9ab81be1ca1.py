import numpy as np

n = 8
p = [0.85, 0.10, 0.05]
results = []

for _ in range(10000):
    sample = np.random.multinomial(n, p)
    result = int(sample[0])
    results.append(result)

print(results)
