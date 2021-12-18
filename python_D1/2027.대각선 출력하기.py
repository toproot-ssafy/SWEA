shap = 0

for i in range(5):
  for l in range(5):
    if l == shap:
      print('#', end="")
    else:
      print('+', end="")
  shap += 1
  print()