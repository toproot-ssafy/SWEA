import sys
sys.stdin = open('2007.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
  Pattern = input()
  patterWord = ''
  for i in range(1, 11):
    word = Pattern[0:i] # 0
    if word == Pattern[i : i+len(word)]:


