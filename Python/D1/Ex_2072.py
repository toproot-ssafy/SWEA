#SW 문제푸는 방법

# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1  

test_case = int(input())

for i in range(test_case):
    
    numbers = list(map(int, input().split()))
    
    total = 0
    #1. 리스트를 순회하면서
    for number in numbers:
        if number % 2:
            #2. 홀수이면 밖에 있는 변수에 더해주기
            total += number
    print(f'#{i+1} {total}')


