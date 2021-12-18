import sys
sys.stdin = open('1938.txt', 'r')

a, b = map(int, input().split())

def calculator(cal, num1, num2):
  if cal == '+':
    return num1 + num2
  if cal == '-':
    return num1 - num2
  if cal == '*':
    return num1 * num2
  if cal == '/':
    return num1 // num2

print(calculator('+', a, b))
print(calculator('-', a, b))
print(calculator('*', a, b))
print(calculator('/', a, b))