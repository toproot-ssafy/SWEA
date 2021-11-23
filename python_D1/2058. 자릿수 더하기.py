import sys
sys.stdin = open("2058.txt", "r")

N = list(map(str, input()))
sumN = 0
for i in range(0,len(N)):
  sumN += int(N[i])
print(sumN)

# while을 사용한 풀이방법
# T = int(input()) #6789
#
# #  1~6789
#
# total_sum = 0
#
# while T >1:
#     total_sum += T % 10
#     T //= 10
#
#
# print(total_sum)