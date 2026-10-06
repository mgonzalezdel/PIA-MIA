valores = [12, 7, 30, 18]

lo, hi = min(valores), max(valores)

norm = [(v - lo)/(hi - lo) for v in valores]