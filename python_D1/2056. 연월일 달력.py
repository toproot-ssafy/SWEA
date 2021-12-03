import sys
sys.stdin = open("2056.txt", "r")

N = int(input())
for n in range(N) :
  numbers = list(map(int, input()))
  year=0
  month=0
  date=0
  for number in numbers :

