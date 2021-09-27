import sys
sys.stdin = open("2070.txt", "r")

TC = int(input()) # 3
for tc in range(1, TC+1):
  numbers = list(map(int, input().split()))
  if numbers[0] > numbers[1]:
    print('#{} >'.format(tc))
  elif numbers[0] < numbers[1]:
    print('#{} <'.format(tc))
  else:
    print('#{} ='.format(tc))