# 2108th, 통계학 | class 2

import sys

N = int(sys.stdin.readline())
num_list = sorted([int(sys.stdin.readline()) for _ in range(N)])

mean = 0
median = 0
mode, max_count, count, last_num, is_second = 0, 1, 1, -4001, False
extent = 0

for num in num_list:
    mean += num
    if num == last_num: count += 1
    else: count = 1

    if count >= max_count:
        if count > max_count:
            mode = num
            max_count = count
            is_second = False
        elif not is_second:
            mode = num
            if num == num_list[0]: pass
            else: is_second = True

    last_num = num

mean = round(mean / N);                 print(mean)
median = num_list[N//2];                print(median)
mode = mode;                            print(mode)
extent = num_list[-1] - num_list[0];    print(extent)

'''
# 참조 답
# sorting 안함, 배열로 접근

from sys import stdin


def sol2108():
    n = int(stdin.readline())
    counts = [0]*8001
    s = 0
    for i in stdin:
        num = int(i)
        counts[num+4000] += 1

    maxc = max(counts)
    mode = mcnt = 0
    idx = 0
    med = None
    mi, ma = 4001, -4001
    for i in range(8001):
        cnt = counts[i]
        if cnt == 0:
            continue

        num = i-4000
        s += num*counts[i]
        if cnt == maxc and mcnt < 2:
            mode = num
            mcnt += 1
        mi = min(mi, num)
        ma = max(ma, num)
        idx += counts[i]
        if idx >= n//2+1 and med == None:
            med = num

    print(round(s/n), med, mode, ma-mi, sep='\n')


if __name__ == '__main__':
    sol2108()
'''