import random
 
results = []
 
for _ in range(10000):
    messages = {
        "Alpha": random.uniform(0, 100),
        "Beta": random.uniform(0, 100),
        "Gamma": random.uniform(0, 100),
        "Delta": random.uniform(0, 100),
    }
    first = min(messages, key=messages.get)
    results.append(first)
 
print(results)