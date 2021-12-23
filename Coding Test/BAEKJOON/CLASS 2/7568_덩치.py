# 7568th, 덩치 | class 2

N = int(input())

size_table = [list(map(int, input().split())) + [1] for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if size_table[i][0] > size_table[j][0] and size_table[i][1] > size_table[j][1]:
            size_table[j][2] += 1
        elif size_table[i][0] < size_table[j][0] and size_table[i][1] < size_table[j][1]:
            size_table[i][2] += 1

    print(size_table[i][2], end=' ')