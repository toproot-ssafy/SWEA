import sys
sys.stdin = open('2005.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
  N = int(input())
  for i in range(N):
    numList = list(map(int, range(i)))
    for j in range(i):