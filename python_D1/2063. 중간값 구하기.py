import sys
sys.stdin = open("2063.txt", "r")

TC = int(input())
numbers = list(map(int, input().split()))
for i in range(len(numbers)-1, 0, -1):
  for j in range(0, i):
    if numbers[j] < numbers[j+1]:
      numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

midNum = numbers[len(numbers)//2]
print(midNum)


