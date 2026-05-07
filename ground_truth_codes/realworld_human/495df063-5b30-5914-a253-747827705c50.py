import random
 
results = []
 
for _ in range(10000):
    counter = 100
    for _ in range(100):
        if random.random() > 0.1:
            counter += 1
    results.append(counter)
 
print(results)