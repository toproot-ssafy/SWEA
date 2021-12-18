import sys
sys.stdin=open('2019.txt', 'r')

number = int(input())

def doubledouble(number):
  numList = [1]
  result = 1
  for i in range(1, number+1):
    result *= 2
    numList.append(result)
  return numList

for i in doubledouble(number): print(i, end=" ")