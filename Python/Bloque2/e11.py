from functools import reduce

lista_num = [1, 2, 4, 7, 12, 3]

print(
    reduce(
        lambda acc, n: acc * n,
        lista_num,
        1
    )
)

lista_palabras = ["hola", "telefono", "papel", "cuadernillo"]

print(
    reduce(
        lambda acc, p: p if len(p) > len(acc) else acc,
        lista_palabras,
        ""
    )
)