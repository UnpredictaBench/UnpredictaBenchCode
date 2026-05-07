import random
 
results = []
 
for _ in range(10000):
    # 3 A's and 3 B's are read one at a time via select()
    # select() picks whichever pipe is ready - either or both can be ready at once
    # Result is some interleaving of AAA and BBB
    
    pool = ['A'] * 3 + ['B'] * 3
    result = []
    
    a_left, b_left = 3, 3
    while a_left > 0 or b_left > 0:
        # select() may see one or both pipes ready
        if a_left > 0 and b_left > 0:
            choice = random.choice(['A', 'B'])
        elif a_left > 0:
            choice = 'A'
        else:
            choice = 'B'
        result.append(choice)
        if choice == 'A':
            a_left -= 1
        else:
            b_left -= 1
 
    results.append("".join(result))
 
print(results)
 