n = int(input("Elige una tabla: "))

for i in range(1, 11):
  res = n * i
  print(f"{n} x {i:2d} = {res:3d}")