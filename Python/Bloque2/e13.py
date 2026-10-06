precios = [11, 9, 4, 12, 34, 5, 17, 54, 10, 21]

total = sum(x *1.21 for x in precios if x >= 10)

print(f"{total:.2f}")