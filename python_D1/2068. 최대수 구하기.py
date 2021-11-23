import sys
sys.stdin = open("2068.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
  numbers = list(map(int, input().split()))
  max_number = 0
  for number in numbers:
    if max_number < number:
      max_number = number
  print("#{} {}".format(tc, max_number))