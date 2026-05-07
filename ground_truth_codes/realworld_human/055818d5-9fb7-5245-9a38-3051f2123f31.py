import random
 
results = []
 
for _ in range(10000):
    objects = ['A', 'B', 'C', 'D', 'E']
    random.shuffle(objects)
    results.append("\n".join(objects))
 
print(results)
 