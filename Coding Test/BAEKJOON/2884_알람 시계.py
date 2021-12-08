<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:10:56 2021

@author: 이충섭
"""

# 2884th, 알람 시계 | class 1

H, M = input().split()

if int(M) >= 45:
    print(H, int(M) - 45)
else:
    if int(H) != 0:
        print(int(H) - 1, int(M) + 15)
    else:
        print(23, int(M) + 15)
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:10:56 2021

@author: 이충섭
"""

# 2884th, 알람 시계 | class 1

H, M = input().split()

if int(M) >= 45:
    print(H, int(M) - 45)
else:
    if int(H) != 0:
        print(int(H) - 1, int(M) + 15)
    else:
        print(23, int(M) + 15)
>>>>>>> 6862cd09be193473899bd9d732d015b318ea42b4
        