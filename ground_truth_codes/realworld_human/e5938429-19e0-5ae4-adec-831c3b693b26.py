import random
 
results = []
 
for _ in range(10000):
    streams = {
        "Red": random.uniform(0, 100),
        "Blue": random.uniform(0, 100),
        "Green": random.uniform(0, 100),
        "Yellow": random.uniform(0, 100),
    }
    first = min(streams, key=streams.get)
    results.append(first)
 
print(results)