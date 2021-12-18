import sys
sys.stdin = open('1936.txt', 'r')

a,b = map(str, input().split())

def winner(A, B):
  if A == '1':
    if B == '2':
      return 'B'
    else:
      return 'A'
  if A == '2':
    if B == '1':
      return 'A'
    else:
      return 'B'
  if A == '3':
    if B == '1':
      return 'B'
    else:
      return 'A'

print(winner(a,b))

