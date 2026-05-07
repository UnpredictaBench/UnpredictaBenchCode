import random

my_list = [8.14, 10.11, 4.23]

results = []

for _ in range(10000):
    shuffled = my_list.copy()
    random.shuffle(shuffled)
    results.append(shuffled)

print(results)