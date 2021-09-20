# n = int(input())
# for i in range(n):
#     lis = list(map(int,input().split()))
#     sum = 0
#     for ele in lis:
#         if ele % 2 != 0:
#             sum += ele
#     print("#" + str(i+1), sum)

import sys
sys.stdin = open("2072.txt", "r")

TC = int(input()) # 3
for tc in range(1, TC+1):
    numbers = list(map(int ,input().split()))
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    print("#{} {}".format(tc, total))