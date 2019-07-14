import itertools
pool = ['A', 'B', 'C']
print(list((map(''.join, itertools.permutations(pool)))))
print(list(map(''.join, itertools.permutations(pool, 2)))) 