def exp(a, b):
  if b == 1:
      return a
  return (a * exp(a, b - 1))
    
a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print("A = ", a, "B = ", b, "-> ",exp(a, b))