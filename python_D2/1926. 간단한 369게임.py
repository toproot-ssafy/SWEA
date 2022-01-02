import sys
sys.stdin = open('1926.txt', 'r')

numList = list(map(str, range(1, int(input())+1)))
strList = []

for i in numList:
  subList = list(i)
  cnt = 0
  for j in subList:
    if j == '3':
      cnt += 1
    elif j == '6':
      cnt += 1
    elif j == '9':
      cnt += 1
  if cnt == 0:
    print(i, end='')
  else:
    for k in range(cnt):
      print('-', end='')
  print(' ', end='')