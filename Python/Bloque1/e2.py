n = float(input("Nota: "))
cal =""

if(0 <= n < 5):
  cal = "Suspenso"
elif(5 <= n < 7):
  cal = "Aprobado"
elif(7 <= n < 9):
  cal = "Notable"
elif(9 <= n <= 10):
  cal = "Sobresaliente"
else:
  cal = "Nota no válida"

print(cal)