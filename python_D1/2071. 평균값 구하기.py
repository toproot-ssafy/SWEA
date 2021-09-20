import sys
sys.stdin = open("2071.txt", "r")

TC = int(input()) # 3
for tc in range(1, TC+1):
    numbers = list(map(int, input().split()))
    total = 0
    for num in numbers:
        total += num
    avg = round(total / 10)
    print("#{} {}".format(tc, avg))