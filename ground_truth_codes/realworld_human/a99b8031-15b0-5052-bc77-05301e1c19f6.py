import random
 
results = []
 
for _ in range(10000):
    # a and b form a reference cycle, so gc.collect() destroys both
    # order of destruction is non-deterministic
    order = ['A', 'B']
    random.shuffle(order)
    results.append("\n".join(order))
 
print(results)
 