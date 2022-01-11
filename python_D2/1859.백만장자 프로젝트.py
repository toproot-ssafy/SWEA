import sys
sys.stdin = open('1859.txt','r')

TC = int(input())

def calPrice(Days):
  MaxNum = Day[-1] # 맨 뒤의 숫자부터 크기 비교
  Day.reverse() # 역순으로 바꾼 후 탐색
  Value = 0 # 시세차익
  for i in Day:
    if i > MaxNum:
      MaxNum = i
    else:
      Value += MaxNum - i
  return Value

for tc in range(TC):
  N = int(input())
  Day = list(map(int, input().split()))
  Result = 0
  Result += calPrice(Day)

  print('#{}'.format(tc+1),Result)