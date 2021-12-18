import sys
sys.stdin = open('1933.txt', 'r')

number = int(input())

def divisor(num):
  numList = []
  for i in range(1, num+1):
    if num % i == 0:
      numList.append(i)
  return numList

result = divisor(number)
for i in result:
  print(i, end=" ")