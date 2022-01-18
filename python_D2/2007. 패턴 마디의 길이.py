import sys
sys.stdin = open('2007.txt', 'r')

def check(wordList):
  cnt = 0
  for p in range(0, 30, len(wordList)): # 주어진 단어의 길이만큼 끊어서 단어와 같은지 확인
    if p+len(wordList)+1 <= 31:
      if Pattern[p:p+len(wordList)] == wordList:
        cnt += 1 # 같다면 1을 카운팅
  if cnt == (len(Pattern)//len(wordList)): # 전체 패턴을 마디별로 나눈 몫과 같으면 true
    return True

TC = int(input())

for tc in range(1, TC+1):
  Pattern = list(input())

  for p in range(1, 10):
    wordList = Pattern[:p]
    if check(wordList):
      print("#{} {}".format(tc, p))
      break