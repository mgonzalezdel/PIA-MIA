from functools import reduce

precios = [11, 9, 4, 12, 34, 5, 17, 54, 10, 21]

print(f"{
    reduce(
        lambda acc, p: acc + p,
        map(
            lambda p: p * 1.21,
            filter(
                lambda p: p >= 10, precios
            )
        ), 0
    ):.2f} €"
)