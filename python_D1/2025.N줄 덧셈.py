import sys
sys.stdin = open('2025.txt', 'r')

number = int(input())
sum = 0
for i in range(1, number+1):
  sum += i
print(sum)