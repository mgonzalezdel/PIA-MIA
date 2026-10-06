import random

n = random.randint(1, 100)
intentos = 5

while(intentos > 0):
  res = int(input("Prueba suerte: "))
  if(res > n):
    print("Menos")
  elif(res < n):
    print("Más")
  else:
    print(f"¡Bingo! Era {n}")
    break
  intentos -= 1
  print(f"Intentos restantes: {intentos}")

if(intentos <= 0 ):
  print("¡Mala suerte!")