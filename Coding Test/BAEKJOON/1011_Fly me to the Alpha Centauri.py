# 1011th, Fly me to the Alpha Centauri | others
import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

for _ in range(int(sinput())):
    x, y = map(int, sinput().split())
    distance = y-x
    count = int(distance ** 0.5) - 1
    while distance > (count+1)*(count+2):
        count += 1

    if distance > (count + 1) ** 2:
        sprint(str(count*2 + 2) + '\n')
    else:
        sprint(str(count*2 + 1) + '\n')

# 다른 방법
'''
for _ in range(int(sinput())):
    # ex) 4, 5, 6, 7
    x, y = map(int, sinput().split())
    distance = y-x

    # distance-1 : 4 <-> 5, 6, 7
    count = int((distance-1) ** 0.5)

    # if statement: 5, 6 <-> 7 | 6 = count^2 + count
    if distance <= count**2 + count:
        print(count*2)
    else:
        print(count*2 + 1)
'''
print('time', time.time() - start)


