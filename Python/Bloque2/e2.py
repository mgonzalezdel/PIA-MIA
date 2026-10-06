numeros = [7, 3, 1, 8, 7, 2, 3, 10]

sin_repetir = []

for i in numeros:
    if(i not in sin_repetir):
        sin_repetir.append(i)

print(sin_repetir)