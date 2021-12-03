import sys
sys.stdin = open("2056.txt", "r")

N = int(input())
for n in range(N):
  numbers = str(input())
  year = numbers[:4]
  month = numbers[4:6]
  date = numbers[6:]

  result = -1

  if (0 < int(month) < 13):
    if int(month) in [2] and (0 < int(date) < 29):
      result = year + '/' + month + '/' + date
    if int(month) in [1, 3, 5, 7, 8, 10, 12] and (0 < int(date) < 32):
      result = year + '/' + month + '/' + date
    if int(month) in [4, 6, 9, 11] and (0 < int(date) < 31):
      result = year + '/' + month + '/' + date

  print('#{} {}'.format(n+1, result))


