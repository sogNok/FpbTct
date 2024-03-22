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


from collections import Counter, deque

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

queue = deque()
queue.append(5)
queue.append(3)
queue.append(1)
queue.append(7)
queue.popleft()
queue.append(4)
queue.append(6)
queue.popleft()

print(queue)
queue.reverse()
print(queue)


import math

a = 21
b = 14

print(math.gcd(21, 14))
print(math.lcm(21, 14))
