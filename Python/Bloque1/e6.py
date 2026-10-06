n = int(input("Elige el límite: "))
a, b = 0, 1

while a <= n:
  print(a, end=" ")
  a, b = b, a+b