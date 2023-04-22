def exp(a, b):
  if b == 1:
      return a
  return (a * exp(a, b - 1))
    

print(exp(3, 5))