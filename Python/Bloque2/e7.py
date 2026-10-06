Y_REAL = ["setosa", "virginica", "setosa", "versicolor"]

Y_PRED = ["setosa", "virginica", "setosa", "setosa"]

aciertos = 0
for a, b in zip(Y_REAL, Y_PRED):
    if a == b:
        aciertos += 1

print(f"Porcentaje de acierto: {(aciertos/len(Y_REAL)) * 100:.2f}%")