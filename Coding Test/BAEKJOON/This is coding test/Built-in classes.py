from itertools import permutations, combinations, product, combinations_with_replacement

data = ['a', 'b', 'c']

result = list(permutations(data, 2))
print(result)

result = list(combinations(data, 3))
print(result)

result = list(product(data, repeat=2))
print(result)

result = list(combinations_with_replacement(data, 2))
print(result)


from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))


import math

a = 21
b = 14

print(math.gcd(21, 14))
print(math.lcm(21, 14))
