import sys
sys.stdin = open('2005.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
  N = int(input())
  for i in range(N): # N번 반복한다 0 1
    # 2중 리스트 만들어서 (자신 -1), (자신) 의 합을 더함
    # -1 했을 때 검사를 통해 범위 체크
    Result = []
    # 첫번째는 무조건 1
    if i == 0:
      Result.append([1])
      break
    for j in range(i): # 1
      # 두번째 부터 그 전 리스트 검사
      # 그 전 리스트의 자신과 같은 숫자
      if (j - 2) > 0:
        Same = Result[j-1][j-1]
        Before = Result[j-1][j-2]

