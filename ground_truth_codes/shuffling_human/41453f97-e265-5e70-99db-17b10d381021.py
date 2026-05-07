import random

my_list = ["apple", "banana"]

results = []

for _ in range(10000):
    shuffled = my_list.copy()
    random.shuffle(shuffled)
    results.append(shuffled)

print(results)