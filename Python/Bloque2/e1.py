notas = [1.2, 5, 4.8, 7.5, 6, 10, 3, 8.3]
notas.sort()
suma=0
aprobadas=0
for i in notas:
    suma += i
    if i >= 5:
        aprobadas += 1
media = suma/len(notas)

print(f"Media: {media} \nMáximo: {notas[-1]} \nMínimo: {notas[0]} \nAprobadas: {aprobadas}")