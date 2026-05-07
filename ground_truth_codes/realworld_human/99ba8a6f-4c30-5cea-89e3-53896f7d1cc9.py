import random
 
results = []
 
for _ in range(10000):
    parent_threads = ["parent-thread-1", "parent-thread-2"]
    child_threads = ["child-thread-1", "child-thread-2"]
 
    # Each process: race condition determines if 1 or 2 threads print
    parent_out = parent_threads if random.random() < 0.1 else [random.choice(parent_threads)]
    child_out = child_threads if random.random() < 0.1 else [random.choice(child_threads)]
 
    # Interleave parent and child output randomly
    combined = parent_out + child_out
    random.shuffle(combined)
 
    results.append("\n".join(combined))
 
print(results)
 