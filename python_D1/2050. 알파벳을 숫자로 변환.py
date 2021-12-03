import string
import sys
sys.stdin = open('2050.txt', 'r')

Alphabet = input()
lowerSample = list(map(chr, range(97, 123)))
upperSample = []
for i in lowerSample:
  upperSample.append(i.upper())

for n in range(len(Alphabet)):
  for d in range(len(upperSample)):
    if Alphabet[n] == upperSample[d]:
      print(d+1, end=' ')




