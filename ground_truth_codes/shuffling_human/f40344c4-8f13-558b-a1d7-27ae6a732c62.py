import random

my_list = ["first", "second", "third"]

results = []

for _ in range(10000):
    shuffled = my_list.copy()
    random.shuffle(shuffled)
    results.append(shuffled)

print(results)