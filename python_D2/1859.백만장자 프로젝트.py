import sys
sys.stdin = open('1859.txt','r')

TC = int(input())
TC = 2
for tc in range(TC):
  N = int(input())
  Day = list(map(int, input().split()))
  print(N, Day)

