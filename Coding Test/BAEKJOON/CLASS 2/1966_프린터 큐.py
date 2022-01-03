# 1966th, 프린터 큐 | class 2

import sys
sinput = sys.stdin.readline

TN = int(sinput())

for _ in range(TN):
    N, M = map(int, sinput().split())
    test_list = list(map(int, sinput().split()))
    num = test_list[M]
    test_list[M] = 0
    max_num = max(test_list)
    itr, count, len_list = 0, 0, len(test_list)
    while max_num > num:
        if itr == len_list: itr = 0

        if test_list[itr] == max_num:
            test_list.pop(itr)
            count += 1
            len_list -= 1


print(test_list)