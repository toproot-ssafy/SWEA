import sys
sys.stdin = open('2029.txt', 'r')

TC = int(input())

for tc in range(TC):
  a, b = map(int, input().split())
  print('#{}'.format(tc+1),a//b, a%b)