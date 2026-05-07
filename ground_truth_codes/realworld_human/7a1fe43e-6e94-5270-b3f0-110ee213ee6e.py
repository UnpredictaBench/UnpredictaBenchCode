import random
 
results = []
 
for _ in range(10000):
    results.append(random.choice(['A', 'B']))
 
print(results)