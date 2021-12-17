import sys
sys.stdin = open('2043.txt', 'r')

numbers = input().split()
P = int(numbers[0]) # 123
K = int(numbers[1]) # 100
count = 0

for i in range(K, P+1):
  count += 1

print(count)